# Projeto Avaliativo do módulo Banco de Dados, do bootcamp Ada Tech

Este repositório contém um código em Python, apresentado em um arquivo Jupyter Notebook chamado `index.ipynb` na pasta questão_1, que aborda a modelagem e normalização de bancos de dados relacionais, juntamente com consultas SQL simples e complexas em um banco de dados MySQL. Este código foi desenvolvido como uma resolução de uma atividade que originalmente propunha o uso do PostgreSQL, mas foi adaptado para o MySQL.

## Atividade 1 - Modelagem e Normalização de Bancos de Dados

O cenário desta atividade envolve a necessidade de projetar um banco de dados para mapear clientes de uma instituição financeira em relação aos produtos financeiros que eles contrataram. O gestor forneceu um esboço inicial do banco de dados com duas tabelas: `cliente` e `produto`. O desafio consistiu em realizar a modelagem conceitual e, em seguida, criar um modelo lógico respeitando as três primeiras formas normais. Os pontos abordados foram:

1. **Modelo Conceitual (Não Normalizado)**
   - Apresentação do modelo conceitual inicial fornecido pelo gestor.
   - Destaque para atributos-chave, atributos multivalorados e cardinalidade dos relacionamentos.

2. **Modelo Lógico (Normalizado)**
   - Apresentação do modelo lógico após a normalização.
   - Destaque para atributos-chave, atributos multivalorados e cardinalidade dos relacionamentos.

![Modelo Conceitual Normalizado](/images/modelo_conceitual_normalizado.jpg)

![Modelo Lógico Normalizado](/images/modelo_logico_normalizado.jpg)

## Consultas SQL

Além da modelagem e normalização, o código também inclui consultas SQL simples e complexas em um banco de dados MySQL. As consultas foram projetadas para atender às seguintes solicitações:

1. Listar os nomes de todos os produtos com preço superior a 100 reais, ordenando-os primeiro pelo preço e depois pelo nome, utilizando aliases para mostrar as colunas de nome e preço.

2. Listar os IDs e preços de produtos cujo preço seja maior do que a média de todos os preços na tabela "produtos".

3. Para cada categoria, mostrar o preço médio do conjunto de produtos associados a ela. As categorias sem produtos associados não devem ser exibidas no resultado.

# Atividade 2: Inserções, Alterações e Remoções de Dados em um Banco de Dados

Este repositório contém um código em Python, apresentado em um arquivo Jupyter Notebook chamado `index.ipynb` na pasta "questão_2", que aborda a realização de operações de inserção, alteração e remoção de dados em um banco de dados MySQL. Esse código faz parte de uma etapa de avaliação para uma posição de cientista de dados na Ada, uma das maiores formadoras do país em áreas relacionadas à tecnologia.

## Descrição da Atividade

Nesta etapa de avaliação, você foi desafiado a demonstrar seu conhecimento em bancos de dados por meio da criação e manipulação de um banco de dados simples que representa um relacionamento 1:n entre as entidades "aluno" e "turma". Para isso, foram fornecidas duas tabelas:

**Tabela 1 - aluno**
- Colunas: id_aluno (INT), nome_aluno (VARCHAR), aluno_alocado (BOOLEAN), id_turma (INT)

**Tabela 2 - turma**
- Colunas: id_turma (INT), código_turma (VARCHAR), nome_turma (VARCHAR)

As etapas da atividade foram as seguintes:

1. Inserir pelo menos duas turmas diferentes na tabela de turma.
2. Inserir pelo menos 1 aluno alocado em cada uma destas turmas na tabela aluno (todos com NULL na coluna aluno_alocado).
3. Inserir pelo menos 2 alunos não alocados em nenhuma turma na tabela aluno (todos com NULL na coluna aluno_alocado).
4. Atualizar a coluna aluno_alocado da tabela aluno, de modo que os alunos associados a uma disciplina recebam o valor True e alunos não associados a nenhuma disciplina recebam o valor False para esta coluna.

## Configuração do Ambiente

O código também inclui comandos para configurar um ambiente Docker com um servidor MySQL. Portanto, antes de executar o código, certifique-se de que o Docker esteja instalado em seu sistema.

## Requisitos

- Docker
- Python 3.x
- Bibliotecas Python: pandas, pymysql

## Execução do Código

Para executar o código, siga estas etapas:

1. Certifique-se de ter o Docker instalado em seu sistema.
2. Execute o comando para criar e iniciar um contêiner Docker com um servidor MySQL.
3. Instale as bibliotecas Python necessárias usando `pip install pandas pymysql`.
4. Execute o código no Jupyter Notebook `index.ipynb`. O código inclui funções para realizar as atividades descritas acima, como criar tabelas, inserir dados e executar consultas SQL.
5. Não se esqueça de encerrar o contêiner Docker após a conclusão da atividade usando `docker container stop turminhadb`. Já presente no fim de seu Jupyter Notebook `index.ipynb`.

Lembre-se de que a criação e inicialização do contêiner Docker podem levar algum tempo, então seja paciente.

Este README fornece uma visão geral do código e das atividades abordadas.
Consulte o arquivo Jupyter Notebook `index.ipynb` em cada uma das pastas referentes a questões 1 e 2 para detalhes completos sobre a implementação.

Divirta-se explorando e aprendendo com este projeto!