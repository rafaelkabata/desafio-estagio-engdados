import json
import pandas as pd
import re
from datetime import datetime
import requests


# Carregar os dados dos clientes do sistema (sistema.xlsx)
dados_sistema = pd.read_excel('sistema.xlsx')

# Carregar os dados dos novos clientes (dados.xlsx)
dados_clientes = pd.read_excel('dados.xlsx')


# Função criada para fazer a validação do CPF
def validar_cpf(cpf):
    cpf = [int(char) for char in cpf if char.isdigit()]

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

# Função para validar nome completo
def validar_nome(nome):
    return len(nome.split()) > 1

# Função para validar data de nascimento no formato 'dd/mm/yyyy'
def validar_data_nascimento(data_nascimento):
    try:
        nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        idade = (datetime.now() - nascimento).days // 365
        return idade >= 18
    except ValueError:
        return False

# Função para validar email
def validar_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Função para validar telefone
def validar_telefone(telefone):
    # Encontra o DDD e o número no formato (99) 98765-4321
    match = re.search(r'\((\d{2})\)\s*(\d{4,5})-(\d{4})', telefone)
    if match:
        ddd = match.group(1)
        numero = match.group(2) + match.group(3)
        return ddd, numero
    else:
        return None, None

# Função para validar CEP e obter detalhes do endereço
def validar_cep(cep, cidade_esperada):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            dados = response.json()
            if 'erro' in dados:
                return False, None
            else:
                endereco = {
                    'cep': dados['cep'],
                    'endereco': dados['logradouro'],
                    'bairro': dados['bairro'],
                    'cidade': dados['localidade'],
                    'estado': dados['uf']
                }
                if dados['localidade'].lower() == cidade_esperada.lower():
                    return True, endereco
                else:
                    return False, None
        else:
            return False, None
    except requests.RequestException:
        return False, None

# Função para validar clientes
def validar_clientes(clientes, dados_sistema):
    clientes_validos = []
    clientes_invalidos = []
    
    for cliente in clientes:
        chaves_necessarias = ['cpf', 'nome', 'data_nascimento', 'email', 'telefone', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'estado', 'ra', 'curso', 'faculdade']
        if not all(chave in cliente for chave in chaves_necessarias):
            cliente['motivo'] = 'Dados incompletos'
            clientes_invalidos.append(cliente)
            continue
        
        cpf_existe = cliente['cpf'] in dados_sistema['cpf'].values
        
        cpf_valido = validar_cpf(cliente['cpf'])
        nome_valido = validar_nome(cliente['nome'])
        data_nascimento_valida = validar_data_nascimento(cliente['data_nascimento'])
        email_valido = validar_email(cliente['email'])
        telefone_valido = validar_telefone(cliente['telefone'])
        cep_valido, endereco = validar_cep(cliente['cep'], cliente['cidade'])
        
        if cpf_valido and nome_valido and data_nascimento_valida and email_valido and telefone_valido and cep_valido:
            if not cpf_existe:
                tipo_acao = 'I'  # Inserção
            else:
                tipo_acao = 'A'  # Atualização
            
            # Corrigindo a extração do DDD e número de telefone
            ddd_telefone = validar_telefone(cliente['telefone'])
            
            cliente_json = {
                "id": f"usp-{cliente['cpf']}",
                "agrupador": "usp",
                "tipoPessoa": "FISICA",
                "nome": cliente['nome'],
                "cpf": cliente['cpf'],
                "dataNascimento": datetime.strptime(cliente['data_nascimento'], '%d/%m/%Y').strftime('%Y-%m-%d'),
                "tipo": tipo_acao,
                "enderecos": [
                    {
                        "cep": cliente['cep'],
                        "logradouro": endereco['endereco'],
                        "bairro": endereco['bairro'],
                        "cidade": endereco['cidade'],
                        "numero": cliente['numero'],
                        "uf": endereco['estado']
                    }
                ],
                "emails": [
                    {
                        "email": cliente['email']
                    }
                ],
                "telefones": [
                    {
                        "tipo": "CELULAR",
                        "ddd": ddd_telefone[0],  # DDD
                        "telefone": ddd_telefone[1]  # Número de telefone
                    }
                ],
                "informacoesAdicionais": [
                    {
                        "campo": "cpf_aluno",
                        "linha": 1,
                        "coluna": 1,
                        "valor": cliente['cpf']
                    },
                    {
                        "campo": "nome_aluno",
                        "linha": 1,
                        "coluna": 1,
                        "valor": cliente['nome']
                    }
                ]
            }
            
            clientes_validos.append(cliente_json)
        else:
            motivo = []
            if not cpf_valido:
                motivo.append('CPF inválido')
            if not nome_valido:
                motivo.append('Nome incompleto')
            if not data_nascimento_valida:
                motivo.append('Data de nascimento inválida ou menor de 18 anos')
            if not email_valido:
                motivo.append('Email inválido')
            if not telefone_valido:
                motivo.append('Telefone inválido')
            if not cep_valido:
                motivo.append('CEP inválido ou não encontrado')
            cliente['motivo'] = ', '.join(motivo)
            clientes_invalidos.append(cliente)
    
    return clientes_validos, clientes_invalidos



# Mapeamento das colunas do arquivo dados.xlsx
mapa_colunas = {
    'NOME': 'nome',
    'CPF': 'cpf',
    'Data de Nascimento': 'data_nascimento',
    'Email': 'email',
    'CEP': 'cep',
    'Endereço': 'endereco',
    'Numero': 'numero',
    'Bairro': 'bairro',
    'Cidade': 'cidade',
    'Estado': 'estado',
    'Telefone': 'telefone',
    'RA': 'ra',
    'Curso': 'curso',
    'Faculdade': 'faculdade'
}

# Renomear colunas de acordo com o mapeamento
dados_clientes.rename(columns=mapa_colunas, inplace=True)

# Verificar se todas as colunas esperadas estão presentes após o mapeamento
colunas_esperadas = ['cpf', 'nome', 'data_nascimento', 'email', 'telefone', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'estado', 'ra', 'curso', 'faculdade']
colunas_faltantes = [col for col in colunas_esperadas if col not in dados_clientes.columns]
if colunas_faltantes:
    raise ValueError(f"Colunas faltantes no arquivo dados.xlsx: {', '.join(colunas_faltantes)}")

# Convertendo a coluna de data de nascimento para strings formatadas
dados_clientes['data_nascimento'] = dados_clientes['data_nascimento'].apply(lambda x: x.strftime('%d/%m/%Y') if isinstance(x, datetime) else x)

# Validar os clientes
clientes_validos, clientes_invalidos = validar_clientes(dados_clientes.to_dict(orient='records'), dados_sistema)

# Salvar clientes válidos em JSON
with open('clientes_para_subir.json', 'w', encoding='utf-8') as file:
    json.dump(clientes_validos, file, ensure_ascii=False, indent=4)

# Salvar clientes inválidos em Excel
df_invalidos = pd.DataFrame(clientes_invalidos)
df_invalidos.to_excel('clientes_invalidos.xlsx', index=False)

print("Processamento concluído.")
