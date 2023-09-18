#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' docker run --name turminhadb -d -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=turminha -p 8081:3306 --rm  mysql:8.1.0')


# In[ ]:


get_ipython().system(' pip install mysql.connector')


# In[2]:


import mysql.connector


# Não execute tudo, pois o banco leva ao menos 45segundos para iniciar o banco.

# In[3]:


# Função para conectar ao banco de dados
def conectar_banco():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',    # Se estiver rodando no mesmo host
            user='root',
            password='123456',
            database='turminha',
            port=8081           # A porta mapeada para o MySQL no container
        )
        if connection.is_connected():
            print("Conexão ao banco de dados MySQL estabelecida com sucesso.")
            return connection
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", str(e))
        return None


# In[4]:


connection = conectar_banco()


# In[5]:


# Criar tabelas
def criar_tabela_aluno(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                id_aluno INT AUTO_INCREMENT PRIMARY KEY,
                nome_aluno VARCHAR(255),
                aluno_alocado BOOLEAN,
                id_turma INT
            )
        """)
        connection.commit()
        print("Tabela aluno criada com sucesso.")
    except Exception as e:
        print("Erro ao criar tabela aluno:", str(e))


# In[6]:


def criar_tabela_turma(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS turma (
                id_turma INT AUTO_INCREMENT PRIMARY KEY,
                codigo_turma VARCHAR(255),
                nome_turma VARCHAR(255)
            )
        """)
        connection.commit()
        print("Tabela turma criada com sucesso.")
    except Exception as e:
        print("Erro ao criar tabela turma:", str(e))



# In[7]:


# Criar as tabelas
criar_tabela_aluno(connection)
criar_tabela_turma(connection)


# a) Inserir pelo menos duas turmas diferentes na tabela de turma:

# In[8]:


def inserir_turmas(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO turma (codigo_turma, nome_turma) VALUES (%s, %s)", ("T1", "Turma 1"))
        cursor.execute("INSERT INTO turma (codigo_turma, nome_turma) VALUES (%s, %s)", ("T2", "Turma 2"))
        connection.commit()
        print("Turmas inseridas com sucesso.")
    except Exception as e:
        print("Erro ao inserir turmas:", str(e))

# Chamando a função para inserir turmas
inserir_turmas(connection)


# b) Inserir pelo menos 1 aluno alocado em cada uma destas turmas na tabela aluno (todos com NULL na coluna aluno_alocado):

# In[9]:


def inserir_alunos(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO aluno (nome_aluno, aluno_alocado, id_turma) VALUES (%s, NULL, %s)", ("Aluno 1", 1))
        cursor.execute("INSERT INTO aluno (nome_aluno, aluno_alocado, id_turma) VALUES (%s, NULL, %s)", ("Aluno 2", 2))
        connection.commit()
        print("Alunos inseridos com sucesso.")
    except Exception as e:
        print("Erro ao inserir alunos:", str(e))

# Chamando a função para inserir alunos
inserir_alunos(connection)


# c) Inserir pelo menos 2 alunos não alocados em nenhuma turma na tabela aluno (todos com NULL na coluna aluno_alocado):

# In[10]:


def inserir_alunos_nao_alocados(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO aluno (nome_aluno, aluno_alocado) VALUES (%s, NULL)", ("Aluno 3",))
        cursor.execute("INSERT INTO aluno (nome_aluno, aluno_alocado) VALUES (%s, NULL)", ("Aluno 4",))
        connection.commit()
        print("Alunos não alocados inseridos com sucesso.")
    except Exception as e:
        print("Erro ao inserir alunos não alocados:", str(e))

# Chamando a função para inserir alunos não alocados
inserir_alunos_nao_alocados(connection)


# d) Atualizar a coluna aluno_alocado da tabela aluno:

# In[11]:


def atualizar_aluno_alocado(connection, aluno_id, alocado):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE aluno SET aluno_alocado = %s WHERE id_aluno = %s", (alocado, aluno_id))
        connection.commit()
        print(f"Aluno {aluno_id} atualizado para alocado = {alocado}.")
    except Exception as e:
        print("Erro ao atualizar aluno:", str(e))

# Atualizar alunos alocados
atualizar_aluno_alocado(connection, 1, True)
atualizar_aluno_alocado(connection, 2, True)

# Atualizar alunos não alocados
atualizar_aluno_alocado(connection, 3, False)
atualizar_aluno_alocado(connection, 4, False)


# In[12]:


get_ipython().system(' docker container stop turminhadb')

