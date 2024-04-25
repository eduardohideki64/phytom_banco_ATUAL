import mysql.connector
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='teste-schema'
    )

    nome = str(input('Digite o nome do produto: '))
    categoria = str(input('Digite a categoria do produto: '))
    valor = str(input('Digite o valor do produto: '))

    cursor = connection.cursor()
    cursor.execute('INSERT INTO produtos (nomeproduto, categoria, valor) VALUES (%s, %s, %s);', (nome, categoria, valor))
    connection.commit()
    cursor.close()
    connection.close()

except Exception as e:
    print(f'erro ao salvar dados {e}')