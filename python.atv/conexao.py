import mysql.connector
try:
    connection= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "teste-schema",
    )
    nome = str(input("Digite seu nome:"))
    email = str(input("Digite seu email:"))
    cel = str(input("Digite seu telefone:"))
    # a variavel %s signicia que é uma variavel String vazia
    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s);"

    cursor = connection.cursor()
    cursor.execute(sql, (nome, email, cel))
    connection.commit()
    cursor.close()
    connection.close()

except Exception as e:
    print(f'Erro ao salvar dados: {e}')