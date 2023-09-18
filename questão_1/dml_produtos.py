def inserir_produtos(conn):
    try:
        cursor = conn.cursor()

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
        cursor.execute(dml_insert_produto)

        dml_insert_produto_sem_categoria = """INSERT INTO produto (nome_produto, descricao_produto, valor) VALUES
                    ('Seguro de Carro', 'Seguro de carro com cobertura mínima', 200.00),
                    ('Seguro de Carro Plus', 'Seguro de vida com cobertura ampla', 500.00);"""
        cursor.execute(dml_insert_produto_sem_categoria)

        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao inserir produtos: ', e)


