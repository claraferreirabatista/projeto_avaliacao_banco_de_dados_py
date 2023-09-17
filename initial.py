#!/usr/bin/env python
# coding: utf-8

# Instalação de um conector, para que façamos uma importação

# In[1]:


get_ipython().system(' pip install mysql-connector-python')


# In[2]:


get_ipython().system(' pip install pymysql')


# In[3]:


import pymysql
import pandas as pd
import warnings
from IPython.display import display, Markdown


# In[4]:


def exibir_markdown(texto_md):
    display(Markdown(texto_md))


# In[5]:


# DESATIVAR ALERTAS
warnings.filterwarnings('ignore')


# In[6]:


import mysql.connector


# In[7]:


try:
  conn = pymysql.connect( user= 'root',
                             host= '127.0.0.1',
                             port= 8080,
                             password= '123456',
                             database= 'LOJINHA')
except pymysql.Error as e:
  print('Erro ao se conectar: ', e)


# In[8]:


cursor = conn.cursor()


# In[9]:


"""admin_user_query = "CREATE USER 'clara'@'%' IDENTIFIED BY 'senhacerta';"
grant_privileges_query = "GRANT ALL PRIVILEGES ON LOJINHA.* TO 'clara'@'%';"

cursor.execute(admin_user_query)
cursor.execute(grant_privileges_query)

# Certifique-se de aplicar as alterações
conn.commit()
"""


# In[10]:


"""user_query = "CREATE USER 'user'@'%' IDENTIFIED BY 'user_password';"
grant_select_query = "GRANT SELECT ON LOJINHA.* TO 'user'@'%';"

cursor.execute(user_query)
cursor.execute(grant_select_query)

# Certifique-se de aplicar as alterações
conn.commit()"""


# In[11]:


drop_exists_cliente_produto = 'DROP TABLE IF EXISTS cliente_produto'
drop_exists_diretor_responsavel = 'DROP TABLE IF EXISTS diretor_responsavel'
drop_exists_categoria = 'DROP TABLE IF EXISTS categoria'
drop_exists_produto = 'DROP TABLE IF EXISTS produto'
drop_exists_tipo_cliente = 'DROP TABLE IF EXISTS tipo_cliente'
drop_exists_cliente = 'DROP TABLE IF EXISTS cliente'


# In[12]:


cursor.execute(drop_exists_cliente_produto)
cursor.execute(drop_exists_cliente)
cursor.execute(drop_exists_tipo_cliente)
cursor.execute(drop_exists_produto)
cursor.execute(drop_exists_categoria)
cursor.execute(drop_exists_diretor_responsavel)



# Sem normalizações 

# In[13]:


"""ddl_cliente = ('''
    CREATE TABLE IF NOT EXISTS cliente (
        codigo_cliente INT AUTO_INCREMENT PRIMARY KEY,
        nome_cliente VARCHAR(255) NOT NULL,
        sobrenome_cliente VARCHAR(255) NOT NULL,
        telefones_cliente VARCHAR(255),
        municipio_cliente VARCHAR(255),
        codigo_tipo_cliente INT,
        tipo_cliente VARCHAR(255)
    )
''')"""


# In[14]:


"""ddl_produto = ('''
    CREATE TABLE IF NOT EXISTS produto (
        codigo_produto INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(255) NOT NULL,
        descricao_produto TEXT,
        codigo_tipo_produto INT,
        tipo_produto VARCHAR(255),
        codigo_diretor_responsavel INT,
        nome_diretor_responsavel VARCHAR(255),
        email_diretor_responsavel VARCHAR(255)
    )
''')"""


# Normalização

# In[15]:


ddl_tipo_cliente = ("""
    CREATE TABLE IF NOT EXISTS tipo_cliente (
        codigo_tipo_cliente INT AUTO_INCREMENT PRIMARY KEY,
        tipo_cliente VARCHAR(255)
    );
""")


# In[16]:


cursor.execute(ddl_tipo_cliente)


# In[17]:


ddl_cliente = ('''
    CREATE TABLE IF NOT EXISTS cliente (
        codigo_cliente INT AUTO_INCREMENT PRIMARY KEY,
        nome_cliente VARCHAR(255) NOT NULL,
        sobrenome_cliente VARCHAR(255) NOT NULL,
        tipo_cliente INT, 
        telefones_cliente VARCHAR(255),
        municipio_cliente VARCHAR(255),
        FOREIGN KEY (tipo_cliente) REFERENCES tipo_cliente(codigo_tipo_cliente) ON DELETE CASCADE
    );
''')


# In[18]:


cursor.execute(ddl_cliente)


# In[19]:


ddl_diretor_responsavel = ("""
    CREATE TABLE IF NOT EXISTS diretor_responsavel (
        codigo_diretor_responsavel INT AUTO_INCREMENT PRIMARY KEY,
        nome_diretor_responsavel VARCHAR(255),
        email_diretor_responsavel VARCHAR(255)
    );

        """)


# In[20]:


cursor.execute(ddl_diretor_responsavel)


# In[21]:


ddl_categoria = ('''
    CREATE TABLE IF NOT EXISTS categoria (
        codigo_categoria INT AUTO_INCREMENT PRIMARY KEY,
        codigo_diretor_responsavel INT,
        tipo_produto VARCHAR(255),
        FOREIGN KEY (codigo_diretor_responsavel) REFERENCES diretor_responsavel(codigo_diretor_responsavel) ON DELETE CASCADE
    );
''')


# In[22]:


cursor.execute(ddl_categoria)


# In[23]:


ddl_produto = ('''
    CREATE TABLE IF NOT EXISTS produto (
        codigo_produto INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(255) NOT NULL,
        descricao_produto TEXT,
        codigo_categoria INT,
        valor DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
        FOREIGN KEY (codigo_categoria) REFERENCES categoria(codigo_categoria) ON DELETE CASCADE
    );
''')


# In[24]:


cursor.execute(ddl_produto)


# In[25]:


conn.commit()


# In[26]:


ddl_cliente_produto = ('''
    CREATE TABLE IF NOT EXISTS cliente_produto (
        codigo_cliente INT,
        codigo_produto INT,
        PRIMARY KEY (codigo_cliente, codigo_produto),
        FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo_cliente) ON DELETE CASCADE,
        FOREIGN KEY (codigo_produto) REFERENCES produto(codigo_produto) ON DELETE CASCADE
    );
''')


# In[27]:


cursor.execute(ddl_cliente_produto)

conn.commit()


# In[28]:


dml_insert_diretor_responsavel = ("""
    INSERT INTO diretor_responsavel (nome_diretor_responsavel, email_diretor_responsavel) VALUES
        ('João Silva', 'joao.silva@bancoclara.com'),
        ('Maria Santos', 'maria.santos@bancoclara.com'),
        ('Pedro Alves', 'pedro.alves@bancoclara.com');
""")


# In[29]:


cursor.execute(dml_insert_diretor_responsavel)


# In[30]:


ddl_insert_categorias_joao_silva = (""" 
INSERT INTO categoria (codigo_diretor_responsavel, tipo_produto) VALUES
    (1, 'Conta Corrente'),
    (1, 'Empréstimos Pessoais'),
    (1, 'Investimentos em Renda Fixa');
""")


# In[31]:


cursor.execute(ddl_insert_categorias_joao_silva)


# In[32]:


ddl_insert_categorias_maria_santos = ("""
INSERT INTO categoria (codigo_diretor_responsavel, tipo_produto) VALUES
    (2, 'Cartões de Crédito'),
    (2, 'Seguros de Vida');
""")


# In[33]:


cursor.execute(ddl_insert_categorias_maria_santos)


# In[34]:


ddl_insert_categorias_pedro_alves = ("""
INSERT INTO categoria (codigo_diretor_responsavel, tipo_produto) VALUES
    (3, 'Internet Banking'),
    (3, 'Pagamentos Eletrônicos'),
    (3, 'Crédito Imobiliário');
""")


# In[35]:


cursor.execute(ddl_insert_categorias_pedro_alves)


# In[36]:


dml_insert_produto = """INSERT INTO produto (nome_produto, descricao_produto, codigo_categoria, valor) VALUES
                      ('Conta Corrente Básica', 'Conta corrente para uso diário', 1, 0.00),
                      ('Conta Corrente Premium', 'Conta corrente com benefícios exclusivos', 1, 10.99),
                      ('Empréstimo Pessoal P1', 'Empréstimo pessoal de curto prazo', 2, 5000.00),
                      ('Empréstimo Pessoal P2', 'Empréstimo pessoal de longo prazo', 2, 10000.00),
                      ('Investimento em Renda Fixa A', 'Investimento de baixo risco', 3, 1000.00),
                      ('Investimento em Renda Fixa B', 'Investimento de médio risco', 3, 5000.00),
                      ('Cartão de Crédito Silver', 'Cartão de crédito com limite moderado', 4, 0.00),
                      ('Cartão de Crédito Gold', 'Cartão de crédito com benefícios premium', 4, 50.00),
                      ('Seguro de Vida Básico', 'Seguro de vida com cobertura mínima', 5, 20.00),
                      ('Seguro de Vida Premium', 'Seguro de vida com cobertura ampla', 5, 50.00),
                      ('Internet Banking App', 'Aplicativo de Internet Banking', 6, 0.00),
                      ('Pagamentos Eletrônicos', 'Sistema de pagamentos online', 7, 0.00),
                      ('Crédito Imobiliário A', 'Crédito para compra de imóveis', 8, 100000.00),
                      ('Crédito Imobiliário B', 'Crédito para construção de imóveis', 8, 150000.00),
                      ('Investimento em Renda Fixa C', 'Investimento de baixo risco', 3, 10000.00),
                      ('Cartão de Crédito Platinum', 'Cartão de crédito com benefícios exclusivos', 4, 100.00),
                      ('Seguro de Vida Premium Plus', 'Seguro de vida com cobertura ampla e extras', 5, 80.00),
                      ('Internet Banking Website', 'Plataforma de Internet Banking', 6, 0.00),
                      ('Crédito Imobiliário C', 'Crédito para compra de imóveis de luxo', 8, 300000.00);

                   
"""


# In[37]:


cursor.execute(dml_insert_produto)


# In[38]:


dml_insert_produto_sem_categoria = """INSERT INTO produto (nome_produto, descricao_produto, valor) VALUES
                    ('Seguro de Carro', 'Seguro de carro com cobertura mínima', 200.00),
                    ('Seguro de Carro Plus', 'Seguro de vida com cobertura ampla', 500.00);"""


# In[39]:


cursor.execute(dml_insert_produto_sem_categoria)


# In[40]:


dml_insert_tipos_cliente = """
INSERT INTO tipo_cliente (tipo_cliente) VALUES
    ('Pessoa Física'),
    ('Pessoa Jurídica'),
    ('Conta Conjunta');
"""


# In[41]:


cursor.execute(dml_insert_tipos_cliente)


# In[42]:


dml_insert_cliente = """ 
INSERT INTO cliente (nome_cliente, sobrenome_cliente, tipo_cliente, telefones_cliente, municipio_cliente) VALUES
    ('João', 'Silva', 1, '123-456-7890', 'São Paulo'),
    ('Maria', 'Santos', 1, '987-654-3210', 'Rio de Janeiro'),
    ('Pedro', 'Alves', 1, '555-555-5555', 'Belo Horizonte'),
    ('Ana', 'Rodrigues', 1, '111-222-3333', 'Porto Alegre'),
    ('Luiz', 'Gomes', 1, '444-444-4444', 'Recife'),
    ('Mariana', 'Fernandes', 1, '777-777-7777', 'Brasília'),
    ('Rafael', 'Oliveira', 2, '222-333-4444', 'Fortaleza'),
    ('Carla', 'Mendes', 2, '999-999-9999', 'Manaus'),
    ('Lucas', 'Pereira', 2, '777-888-9999', 'Salvador'),
    ('Isabela', 'Lima', 2, '666-666-6666', 'Curitiba'),
    ('José', 'Dias', 3, '123-321-1234', 'Goiânia'),
    ('Fernanda', 'Martins', 3, '987-987-9876', 'Natal'),
    ('Gustavo', 'Ferreira', 3, '555-666-7777', 'Florianópolis'),
    ('Camila', 'Ramos', 1, '888-888-8888', 'Maceió'),
    ('Antônio', 'Cavalcante', 1, '777-555-4444', 'Vitória'),
    ('Patrícia', 'Costa', 2, '123-555-9999', 'Porto Velho'),
    ('Roberto', 'Sousa', 2, '333-444-5555', 'Teresina'),
    ('Amanda', 'Oliveira', 3, '111-222-3333', 'João Pessoa'),
    ('Ricardo', 'Silveira', 3, '444-333-2222', 'Cuiabá'),
    ('Larissa', 'Fernandes', 1, '777-999-5555', 'Aracaju'),
    ('Marcelo', 'Carvalho', 1, '666-777-8888', 'Campo Grande'),
    ('Sandra', 'Gonçalves', 1, '555-666-7777', 'Boa Vista'),
    ('Carlos', 'Santana', 2, '222-333-4444', 'Palmas'),
    ('Tatiana', 'Mendes', 2, '999-888-7777', 'Porto Alegre'),
    ('Fábio', 'Ribeiro', 2, '111-222-3333', 'São Luís'),
    ('Vanessa', 'Lima', 1, '555-444-3333', 'Manaus'),
    ('Eduardo', 'Oliveira', 1, '777-777-7777', 'Salvador'),
    ('Márcia', 'Sousa', 1, '123-123-1234', 'Goiânia'),
    ('Paulo', 'Ferreira', 1, '777-888-9999', 'Natal'),
    ('Cristina', 'Costa', 2, '666-555-4444', 'Florianópolis'),
    ('Raul', 'Santos', 2, '333-222-1111', 'João Pessoa'),
    ('Lívia', 'Oliveira', 3, '888-888-8888', 'Belém'),
    ('Mateus', 'Carvalho', 3, '999-999-9999', 'Maceió'),
    ('Fernando', 'Gonçalves', 1, '111-111-1111', 'Aracaju'),
    ('Sônia', 'Santos', 1, '444-555-6666', 'Palmas'),
    ('Alberto', 'Lima', 1, '333-333-3333', 'Cuiabá'),
    ('Aline', 'Oliveira', 2, '111-222-3333', 'Porto Velho'),
    ('Milton', 'Sousa', 2, '555-555-5555', 'Teresina');
"""


# In[43]:


cursor.execute(dml_insert_cliente)


# In[44]:


ddl_view_produtos = '''
    CREATE VIEW produtos_maior_que_100 AS
    SELECT nome_produto AS Produto, valor AS Valor
    FROM produto
    WHERE valor > 100
    ORDER BY valor, nome_produto;
'''


# In[45]:


cursor.execute(ddl_view_produtos)


# In[ ]:


conn.commit()


# In[ ]:


dql_produtos_caros = 'SELECT * FROM produtos_maior_que_100;'



# In[ ]:


cursor.execute(dql_produtos_caros)


# In[ ]:


resultados = cursor.fetchall()


# criar uma visualização com pandas

# In[ ]:


for resultado in resultados:
    print(resultado)


# In[ ]:


dql_media_valor = """
    SELECT codigo_produto, valor FROM produto
    WHERE valor > (SELECT AVG(valor) FROM produto);
"""


# In[ ]:


cursor.execute(dql_media_valor)


# In[ ]:


resultados = cursor.fetchall()


# In[ ]:


for resultado in resultados:
    print(resultado)


# In[47]:


dql_media_categoria = """
SELECT categoria.tipo_produto AS NOME, AVG(produto.valor) as MEDIA FROM produto
        INNER JOIN categoria
            ON produto.codigo_categoria = categoria.codigo_categoria
            GROUP BY categoria.codigo_categoria
            ORDER BY categoria.tipo_produto;
"""


# In[48]:


cursor.execute(dql_media_categoria)


# In[49]:


resultados = cursor.fetchall()


# In[50]:


for resultado in resultados:
    print(resultado)

