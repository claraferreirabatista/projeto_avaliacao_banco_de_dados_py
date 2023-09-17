def listar_media_preco_por_categoria(conn):
    try:
        cursor = conn.cursor()

        dql_media_categoria = """
        SELECT categoria.tipo_produto AS Categoria, AVG(produto.valor) as PreçoMédio
        FROM categoria
        LEFT JOIN produto ON categoria.codigo_categoria = produto.codigo_categoria
        GROUP BY categoria.tipo_produto
        HAVING PreçoMédio IS NOT NULL
        ORDER BY categoria.tipo_produto;
        """
        cursor.execute(dql_media_categoria)

        resultados = cursor.fetchall()

        # Converter os resultados em um DataFrame do Pandas
        df = pd.DataFrame(resultados, columns=['Categoria', 'Preço Médio'])

        # Exibir o DataFrame com Pandas
        print(df)

    except pymysql.Error as e:
        raise Exception('Erro ao listar a média de preço por categoria: ', e)
    finally:
        cursor.close()
