def inserir_tipos_cliente(conn):
    try:
        cursor = conn.cursor()

        dml_insert_tipos_cliente = """
        INSERT INTO tipo_cliente (tipo_cliente) VALUES
            ('Pessoa Física'),
            ('Pessoa Jurídica'),
            ('Conta Conjunta');
        """
        cursor.execute(dml_insert_tipos_cliente)

        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao inserir tipos de cliente: ', e)
    finally:
        cursor.close()

def inserir_clientes(conn):
    try:
        cursor = conn.cursor()

        dml_insert_cliente = """ 
        INSERT INTO cliente (nome_cliente, sobrenome_cliente, tipo_cliente, telefones_cliente, municipio_cliente) VALUES
            ('João', 'Silva', 1, '123-456-7890', 'São Paulo'),
            ('Maria', 'Santos', 1, '987-654-3210', 'Rio de Janeiro'),
            ('Pedro', 'Alves', 1, '555-555-5555', 'Belo Horizonte'),
            ('Ana', 'Rodrigues', 1, '111-222-3333', 'Porto Alegre'),
            ('Luiz', 'Gomes', 1, '444-444-4444', 'Recife'),
            ('Mariana', 'Fernandes', 1, '777-777-7777', 'Brasília'),
            ('Rafael', 'Oliveira', 2, '222-333-4444', 'Fortaleza'),
            ('Carla', 'Mendes', 2, '999-999-9999', 'Manaus'),
            ('Lucas', 'Pereira', 2, '777-888-9999', 'Salvador'),
            ('Isabela', 'Lima', 2, '666-666-6666', 'Curitiba'),
            ('José', 'Dias', 3, '123-321-1234', 'Goiânia'),
            ('Fernanda', 'Martins', 3, '987-987-9876', 'Natal'),
            ('Gustavo', 'Ferreira', 3, '555-666-7777', 'Florianópolis'),
            ('Camila', 'Ramos', 1, '888-888-8888', 'Maceió'),
            ('Antônio', 'Cavalcante', 1, '777-555-4444', 'Vitória'),
            ('Patrícia', 'Costa', 2, '123-555-9999', 'Porto Velho'),
            ('Roberto', 'Sousa', 2, '333-444-5555', 'Teresina'),
            ('Amanda', 'Oliveira', 3, '111-222-3333', 'João Pessoa'),
            ('Ricardo', 'Silveira', 3, '444-333-2222', 'Cuiabá'),
            ('Larissa', 'Fernandes', 1, '777-999-5555', 'Aracaju'),
            ('Marcelo', 'Carvalho', 1, '666-777-8888', 'Campo Grande'),
            ('Sandra', 'Gonçalves', 1, '555-666-7777', 'Boa Vista'),
            ('Carlos', 'Santana', 2, '222-333-4444', 'Palmas'),
            ('Tatiana', 'Mendes', 2, '999-888-7777', 'Porto Alegre'),
            ('Fábio', 'Ribeiro', 2, '111-222-3333', 'São Luís'),
            ('Vanessa', 'Lima', 1, '555-444-3333', 'Manaus'),
            ('Eduardo', 'Oliveira', 1, '777-777-7777', 'Salvador'),
            ('Márcia', 'Sousa', 1, '123-123-1234', 'Goiânia'),
            ('Paulo', 'Ferreira', 1, '777-888-9999', 'Natal'),
            ('Cristina', 'Costa', 2, '666-555-4444', 'Florianópolis'),
            ('Raul', 'Santos', 2, '333-222-1111', 'João Pessoa'),
            ('Lívia', 'Oliveira', 3, '888-888-8888', 'Belém'),
            ('Mateus', 'Carvalho', 3, '999-999-9999', 'Maceió'),
            ('Fernando', 'Gonçalves', 1, '111-111-1111', 'Aracaju'),
            ('Sônia', 'Santos', 1, '444-555-6666', 'Palmas'),
            ('Alberto', 'Lima', 1, '333-333-3333', 'Cuiabá'),
            ('Aline', 'Oliveira', 2, '111-222-3333', 'Porto Velho'),
            ('Milton', 'Sousa', 2, '555-555-5555', 'Teresina');


        """
        cursor.execute(dml_insert_cliente)

        conn.commit()
    except pymysql.Error as e:
        raise Exception('Erro ao inserir clientes: ', e)
    finally:
        cursor.close()
