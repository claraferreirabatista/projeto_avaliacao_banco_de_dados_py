import pymysql

# Função para conectar ao banco de dados
def conectar_db():
    try:
        conn = pymysql.connect(
            user='root',
            host='127.0.0.1',
            port=8080,
            password='123456',
        )
        return conn
    except pymysql.Error as e:
        raise Exception('Erro ao se conectar: ', e)