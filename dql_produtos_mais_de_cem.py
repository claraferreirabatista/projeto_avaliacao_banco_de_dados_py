def listar_produtos_mais_de_100(conn):
    try:
        cursor = conn.cursor()

        dql_produtos_caros = '''
        SELECT nome_produto AS Produto, valor AS Valor
        FROM produto
        WHERE valor > 100
        ORDER BY valor, nome_produto;
        '''
        cursor.execute(dql_produtos_caros)

        resultados = cursor.fetchall()

        # Converter os resultados em um DataFrame do Pandas
        df = pd.DataFrame(resultados, columns=['Produto', 'Valor'])

        # Exibir o DataFrame com Pandas
        print(df)
    except pymysql.Error as e:
        raise Exception('Erro ao listar produtos caros: ', e)
    finally:
        cursor.close()

