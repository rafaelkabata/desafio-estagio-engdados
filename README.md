# Desafio do programa de estágio

</div>

 ## [Arquivos para entrega](https://github.com/rafaelkabata/desafio-estagio-engdados/tree/main/Entregaveis) : Nesta sessão estão os arquivos solicitados para a entrega do desafio.
 ## [Imagens](https://github.com/rafaelkabata/desafio-estagio-engdados/tree/main/Imagens) : Nesta sessão estão as imagens utilizadas para a explicação do desafio.
 ## [Arquivos do desafio](https://github.com/rafaelkabata/desafio-estagio-engdados/tree/main/arquivos_desafio) : Nesta sessão estão os arquivos utilizados para a análise dos dados do script e fornecidos no desafio.

 </div>
 
 <br>
 
### O objetivo do desafio é  realizar a validação e integração de novos clientes em um sistema, certificando se  que os dados sejam consistentes e estejam corretos antes de serem inseridos ou atualizados na base de dados.

</div>



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

Aqui a função faz a validação do cep utilizando a API da viacep. Ele faz uma comparação para verificar se o cep realmente existe e se pertence a cidade. Caso haja uma divergencia entre cep e cidade, a função consegue reconhecer o erro.
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
Por fim, o script renomeia as colunas do DataFrame dados_clientes usando o mapeamento definido anteriormente, cria uma lista (colunas_esperadas) com todos os nomes de colunas que devem estar presentes no DataFrame após o mapeamento então verifica se alguma dessas colunas está faltando. Se houver colunas faltantes, ele lança um erro com uma mensagem indicando quais colunas estão faltando, converte os valores na coluna data_nascimento para strings no formato dd/mm/yyyy, garantindo que todas as datas estejam no mesmo formato de string, verifica a validade dos dados dos clientes. Ele passa os dados dos clientes convertidos para uma lista de dicionários e o DataFrame dados_sistema para a função. A função retorna duas listas: clientes_validos e clientes_invalidos, salva a lista de clientes válidos em um arquivo JSON chamado clientes_para_subir.json e finalmente, o script cria um DataFrame com a lista de clientes inválidos (clientes_invalidos) e salva esse DataFrame em um arquivo Excel chamado clientes_invalidos.xlsx.


![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/fim_codigo.png)


