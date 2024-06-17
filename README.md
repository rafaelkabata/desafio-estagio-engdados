# Desafio do programa de estágio

</div>

 ## [Arquivos para entrega](https://github.com/rafaelkabata/desafio-estagio-engdados/tree/main/Entregaveis) : Nesta seção estão os arquivos solicitados para a entrega do desafio.
 ## [Imagens](https://github.com/rafaelkabata/desafio-estagio-engdados/tree/main/Imagens) : Nesta seção estão as imagens utilizadas para a explicação do desafio.
 ## [Arquivos do desafio](https://github.com/rafaelkabata/desafio-estagio-engdados/tree/main/arquivos_desafio) : Nesta seção estão os arquivos utilizados para a análise dos dados do script e fornecidos no desafio.

 </div>
 
 <br>

  </div>
 
### O objetivo do desafio é  realizar a validação e integração de novos clientes em um sistema, certificando se  que os dados sejam consistentes e estejam corretos antes de serem inseridos ou atualizados na base de dados.

</div>

#### Enunciado do desafio : <br>
Você foi atarefado de subir no sistema novos clientes. Esses clientes devem ser subidos por um arquivo no formato JSON (segue exemplo de como o formato deve ser em "dados.json"), mas antes disso é necessário realizar algumas validações:

O CPF do cliente é válido?
O cliente possui nome completo ?
A data de nascimento é válida? É uma idade possível? (Maiores de 17 anos)
O email é válido?
O Telefone informado esta no formato certo?
Após essas verificações lhe foi dado um modelo da base que se encontra em um determinado sistema ("sistema.xlsx"), os clientes que você recebeu são novos clientes? Quem já está na base? É necessário atualizar os dados?

Ao final do exercício desejamos algumas coisas; um arquivo.py do script que será rodado em outra base para testar sua validação e eficácia. Um arquivo.md explicando a sua resolução e sua forma de pensamento. O arquivo JSON dos clientes para subir no sistema, e um arquivo xlsx com os clientes que não podem subir no sistema e o seu motivo. É importante lembrar que seu código deve ser legível e padronizado.

Notas:

o "TIPO" no arquivo JSON se refere se é um cliente de inserção (I) ou de atualização (A).

o "id" do cliente segue a convenção: faculdade-cpf

DESAFIO BÔNUS:

Sua entrega não é obrigatória mas aquele que conseguir terá um grande destaque no final.

Valide o CEP e Endereço informados, utlizando-se da API: https://viacep.com.br/
 
</div>

# Início


#### Importação das bibliotecas
O script utiliza várias bibliotecas em Python para manipular e validar os dados. A biblioteca json é usada para salvar dados em formato JSON. O pandas ajuda na leitura, manipulação e validação de dados de planilhas Excel. O módulo re é utilizado para trabalhar com expressões regulares, especialmente na extração de informações de números de telefone. O datetime é utilizado para validar as datas de nascimento (Acima de 17 anos). Por fim, requests permite fazer requisições HTTP para validar CEPs e obter detalhes de endereço através da API ViaCEP. 
<br> <br>

![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/bibliotecas.png)

<br>

</div>

#### Carregamento dos dados/criação dos DataFrames

Após importar as bibliotecas necessárias para manipular dados em Python, o script carrega dois arquivos Excel específicos: um chamado sistema.xlsx e outro chamado dados.xlsx. Esses arquivos contêm informações sobre clientes armazenadas em planilhas. Ao carregar esses arquivos, o script os transforma em estruturas de dados chamadas DataFrames, que são como tabelas onde cada linha representa um cliente e cada coluna representa um tipo de informação, como nome, CPF, data de nascimento,dentre outros. Essa etapa permite que o script processe e analise esses dados para realizar tarefas como validação de informações.
<br> <br>

![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/dataframes.png)

</div>

#### Funções de validação

Após o carregando dos dados, foram criadas funções para fazer as validações das informações dos clientes como se o CPF é verdadeiro, está com os 11 digitos e se o seu código de segurança está correto. Também uma função para validar o nome do cliente, ele verifica se no sistema o nome do cliente é maior do que 1. <br>
![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/funcao_1.png)

<br>

Assim como função para validar a data de nascimento no formato que se encontra no xlsx, dd/mm/yyyy. Função para validação de email e função para validar o número correto de telefone ou celular do cliente. <br>
![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/funcao_2.png)

<br>

Aqui a função faz a validação do cep utilizando a API da viacep. Ele faz uma comparação para verificar se o cep realmente existe e se pertence a cidade. Caso haja uma divergencia entre cep e cidade, a função consegue reconhecer o erro. Optei por não comparar com bairro, pois em cidades menores existe apenas 1 cep para a cidade inteira (como na minha) e o cep joga como centro da cidade não fazendo distinção entre os bairros.
![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/funcao_3.png)

<br>

E por fim, a função para validação das informações do cliente e se estivesse tudo ok, seria uma inserção ou atualização para ser enviada para o json. <br>
![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/funcao_4.png) <br>

#### Criando o json 
Nesta parte do código é puxado os dados dos clientes para a criação do json que será enviado para o sistema.
![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/correcao.png) <br>

Esta parte cria um dicionário (mapa_colunas) que mapeia os nomes das colunas no arquivo dados.xlsx para novos nomes  padronizados  que serão usados no DataFrame.

![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/mapeamento%20das%20colunas.png)

<br>

#### Final
Por fim, o script renomeia as colunas do DataFrame dados_clientes usando o mapeamento definido anteriormente, cria uma lista (colunas_esperadas) com todos os nomes de colunas que devem estar presentes no DataFrame após o mapeamento então verifica se alguma dessas colunas está faltando. Se houver colunas faltantes, ele lança um erro com uma mensagem indicando quais colunas estão faltando, converte os valores na coluna data_nascimento para strings no formato dd/mm/yyyy, garantindo que todas as datas estejam no mesmo formato de string, verifica a validade dos dados dos clientes. Ele passa os dados dos clientes convertidos para uma lista de dicionários e o DataFrame dados_sistema para a função. A função retorna duas listas: clientes_validos e clientes_invalidos, salva a lista de clientes válidos em um arquivo JSON chamado clientes_para_subir.json e finalmente, o script cria um DataFrame com a lista de clientes inválidos (clientes_invalidos) e salva esse DataFrame em um arquivo Excel chamado clientes_invalidos.xlsx.


![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/fim_codigo.png)

<br>

#### Clientes_invalidos
Após o script rodar, ele gera um arquivo clientes_invalidos.xlsx contendo as informações e o motivo dos clientes estarem com os dados invalidos.

![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/clientes_invalidos.png)

<br>

#### Clientes para mandar para o sistema Json
Os clientes que estão com as informações corretas são organizados em um arquivo json contendo sua informações como na imagem abaixo. Podemos notar que quando é uma informação que não continha ainda no sistema.xlsx ele classifica o tipo como "I" de inserção

![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/clientes_para_subir.png)

<br>

Enquanto que quando a informação do cliente já continha no sistema, ele acaba apenas fazendo uma atualização "A".
<br>
![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/clientes_para_subir_2.png)

<br>

</div>

## AGRADECIMENTO 

<br>
Agradeço a oportunidade de estar participando do processo seletivo de estágio da Principia. Estou muito animado com a possibilidade de fazer parte desta jovem Hub de soluções financeiras e poder ajudar a construir e fazer diferença na vida de estudantes de todo o país.
Estou a disposição para esclarecer qualquer dúvida a respeito do desafio. <br>
meus contatos são : kabatarafael@gmail.com ou https://www.linkedin.com/in/rafaelkabata/ <br>

Atenciosamente, Rafael Kabata




