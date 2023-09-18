def criar_tabela_cliente_produto(conn):
    try:
        cursor = conn.cursor()

        ddl_cliente_produto = ('''
            CREATE TABLE IF NOT EXISTS cliente_produto (
                codigo_cliente INT,
                codigo_produto INT,
                PRIMARY KEY (codigo_cliente, codigo_produto),
                FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo_cliente) ON DELETE CASCADE,
                FOREIGN KEY (codigo_produto) REFERENCES produto(codigo_produto) ON DELETE CASCADE
            );
        ''')
        cursor.execute(ddl_cliente_produto)

        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao criar tabela cliente_produto: ', e)


