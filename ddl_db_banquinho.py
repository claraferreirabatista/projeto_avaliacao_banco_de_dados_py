def criar_banquinho(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS banquinho")
    except pymysql.Error as e:
        raise Exception('Erro ao criar o banco de dados: ', e)
    finally:
        cursor.close()