def listar_ids_e_precos_acima_media(conn):
    try:
        cursor = conn.cursor()

        dql_media_valor = """
        SELECT codigo_produto, valor
        FROM produto
        WHERE valor > (SELECT AVG(valor) FROM produto);
        """
        cursor.execute(dql_media_valor)

        resultados = cursor.fetchall()

        # Converter os resultados em um DataFrame do Pandas
        df = pd.DataFrame(resultados, columns=['ID', 'Preço'])

        # Exibir o DataFrame com Pandas
        print(df)

    except pymysql.Error as e:
        raise Exception('Erro ao listar ids e preços acima da média: ', e)
    finally:
        cursor.close()
