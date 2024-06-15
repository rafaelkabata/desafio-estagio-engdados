# Desafio do programa de estágio

</div>

### O objetivo do desafio é  realizar a validação e integração de novos clientes em um sistema, certificando se  que os dados sejam consistentes e estejam corretos antes de serem inseridos ou atualizados na base de dados.

</div>

#### Importação das bibliotecas
O script utiliza várias bibliotecas em Python para manipular e validar os dados. A biblioteca json é usada para salvar dados em formato JSON. O pandas ajuda na leitura, manipulação e validação de dados de planilhas Excel. O módulo re é utilizado para trabalhar com expressões regulares, especialmente na extração de informações de números de telefone. O datetime é utilizado para validar as datas de nascimento (Acima de 17 anos). Por fim, requests permite fazer requisições HTTP para validar CEPs e obter detalhes de endereço através da API ViaCEP. 
<br> <br>

![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/bibliotecas.png)

<br>

Após importar as bibliotecas necessárias para manipular dados em Python, o script carrega dois arquivos Excel específicos: um chamado sistema.xlsx e outro chamado dados.xlsx. Esses arquivos contêm informações sobre clientes armazenadas em planilhas. Ao carregar esses arquivos, o script os transforma em estruturas de dados chamadas DataFrames, que são como tabelas onde cada linha representa um cliente e cada coluna representa um tipo de informação, como nome, CPF, data de nascimento,dentre outros. Essa etapa permite que o script processe e analise esses dados para realizar tarefas como validação de informações.
<br> <br>

![Diagrama](https://github.com/rafaelkabata/desafio-estagio-engdados/blob/main/Imagens/dataframes.png)
