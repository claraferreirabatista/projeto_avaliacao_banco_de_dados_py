def inserir_diretores(conn):
    try:
        cursor = conn.cursor()

        dml_insert_diretor_responsavel = ("""
            INSERT INTO diretor_responsavel (nome_diretor_responsavel, email_diretor_responsavel) VALUES
                ('João Silva', 'joao.silva@bancoclara.com'),
                ('Maria Santos', 'maria.santos@bancoclara.com'),
                ('Pedro Alves', 'pedro.alves@bancoclara.com');
        """)
        cursor.execute(dml_insert_diretor_responsavel)

        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao inserir diretores: ', e)
    finally:
        cursor.close()

def inserir_categorias(conn):
    try:
        cursor = conn.cursor()

        dml_insert_categorias_joao_silva = ("""
            INSERT INTO categoria (codigo_diretor_responsavel, tipo_produto) VALUES
                (1, 'Conta Corrente'),
                (1, 'Empréstimos Pessoais'),
                (1, 'Investimentos em Renda Fixa');
        """)
        cursor.execute(dml_insert_categorias_joao_silva)

        dml_insert_categorias_maria_santos = ("""
            INSERT INTO categoria (codigo_diretor_responsavel, tipo_produto) VALUES
                (2, 'Cartões de Crédito'),
                (2, 'Seguros de Vida');
        """)
        cursor.execute(dml_insert_categorias_maria_santos)

        dml_insert_categorias_pedro_alves = ("""
            INSERT INTO categoria (codigo_diretor_responsavel, tipo_produto) VALUES
            (3, 'Internet Banking'),
            (3, 'Pagamentos Eletrônicos'),
            (3, 'Crédito Imobiliário');
        """)

        cursor.execute(dml_insert_categorias_pedro_alves)

        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao inserir categorias: ', e)
    finally:
        cursor.close()

