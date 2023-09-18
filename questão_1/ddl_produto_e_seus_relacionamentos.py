def criar_tabelas_produtos(conn):
    try:
        cursor = conn.cursor()

        ddl_diretor_responsavel = ("""
            CREATE TABLE IF NOT EXISTS diretor_responsavel (
                codigo_diretor_responsavel INT AUTO_INCREMENT PRIMARY KEY,
                nome_diretor_responsavel VARCHAR(255),
                email_diretor_responsavel VARCHAR(255)
            );
        """)
        cursor.execute(ddl_diretor_responsavel)

        ddl_categoria = ('''
            CREATE TABLE IF NOT EXISTS categoria (
                codigo_categoria INT AUTO_INCREMENT PRIMARY KEY,
                codigo_diretor_responsavel INT,
                tipo_produto VARCHAR(255),
                FOREIGN KEY (codigo_diretor_responsavel) REFERENCES diretor_responsavel(codigo_diretor_responsavel) ON DELETE CASCADE
            );
        ''')
        cursor.execute(ddl_categoria)

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
        cursor.execute(ddl_produto)

        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao criar tabelas de produtos: ', e)

