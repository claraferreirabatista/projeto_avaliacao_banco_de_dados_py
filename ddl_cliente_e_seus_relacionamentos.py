def criar_tabela_tipo_cliente(conn):
    cursor = conn.cursor()

    try:
        ddl_tipo_cliente = ("""
            CREATE TABLE IF NOT EXISTS tipo_cliente (
                codigo_tipo_cliente INT AUTO_INCREMENT PRIMARY KEY,
                tipo_cliente VARCHAR(255)
            );
        """)
        cursor.execute(ddl_tipo_cliente)
        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao criar tabela tipo_cliente: ', e)

def criar_tabela_cliente(conn):
    cursor = conn.cursor()

    try:
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
        cursor.execute(ddl_cliente)
        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao criar tabela cliente: ', e)

