import mysql.connector
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="teste-schema"
    )
except Exception as e:
    print(f'Erro ao conectar ao banco de dados: {e}')

def resposta_menu(menu):
    try:
        cursor = connection.cursor()

        if menu == 1:  # cadastrar cliente
            nome = str(input("Digite seu nome: "))
            email = str(input("Digite seu email: "))
            cel = str(input("Digite seu telefone: "))
            sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s);"

            cursor.execute(sql, (nome, email, cel))
            connection.commit()
            print("Cliente cadastrado com sucesso!")


        elif menu == 2: #cadastrar produto
                nome = str(input('Digite o nome do produto: '))
                categoria = str(input('Digite a categoria do produto: '))
                valor = str(input('Digite o valor do produto: '))
                estoque = str(input("Digite a quantidade no estoque"))

                cursor = connection.cursor()
                cursor.execute('INSERT INTO produtos (nomeproduto, categoria, valor, estoque) VALUES (%s, %s, %s, %s);', (nome, categoria, valor, estoque))
                connection.commit()
                cursor.close()
                connection.close()
                print("Produto cadastrado com sucesso!")

        elif menu == 3:#cadastrar venda
                valor_uni = str(input("Digite o valor da unidade: "))
                categoria = str(input("Digite a categoria: "))
                marca = str(input("Digite a marca: "))
                preco_venda = str(input("Digite o preço da venda: "))
                quantidade = str(input("Digite a quantidade de itens vendidos: "))
                sql = "INSERT INTO vendas (valor_unic, ID_categoria, marca, preco_venda, quantidade_venda) VALUES (%s, %s, %s, %s, %s);"

                cursor.execute(sql, (valor_uni, categoria, marca, preco_venda, quantidade))
                connection.commit()
                print("Venda feita!")


        elif menu == 4: #listar produto
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM produtos")
                print("Produtos:")
                for produto in cursor:
                    print(produto)  # Isso imprimirá cada linha como uma tupla
                    cursor.close()
                    connection.close()



        elif menu == 5: #listar cliente
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM clientes")
                print("Clientes:")
                for produto in cursor:
                    print(produto) 
                    cursor.close()
                    connection.close()


        elif menu == 6: #listar vendas
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM vendas")
                print("Vendas:")
                for produto in cursor:
                    print(produto) 
                    cursor.close()
                    connection.close()

            


        elif menu == 7: #UPDATE no banco de dados
           
                new_email = str(input("Digite qual email deseja alterar: "))
                customer_id = int(input("Digite qual cliente deseja alterar: "))
                sql = "UPDATE clientes SET email = %s WHERE id = %s;"
                cursor = connection.cursor()
                cursor.execute(sql, ( new_email, customer_id))
                connection.commit()
        
        
        elif menu == 8: #deletar cliente pelo id
                id = int(input("Digite o ID da pessoa que quer deletar "))
                sql = "DELETE FROM clientes WHERE id = %s;"

                cursor.execute(sql, (id,))
                connection.commit()
                print("Cliente deletado com sucesso!")

            
        
        elif menu == 9: #deletar produto por id
                idproduto = int(input("Digite o ID do produto que quer deletar "))
                sql = "DELETE FROM produtos WHERE idproduto = %s;"

                cursor.execute(sql, (idproduto,))
                connection.commit()
                print("Produto deletado com sucesso!")

        
        
        elif menu == 10: #deletar venda pelo id
                idvenda = int(input("Digite o ID do produto que quer deletar "))
                sql = "DELETE FROM vendas WHERE idvendas = %s;"

                cursor.execute(sql, (idvenda,))
                connection.commit()
                print("Venda deletada com sucesso!")

        

        else:
            print("Opção inválida")
    except Exception as e:
        print(f'Erro ao executar operação: {e}')
    finally:
        cursor.close()


def main():
    menu = int(input("Digite a operação: "))
    resposta_menu(menu)
    connection.close()
    # Esta linha verifica se o script está sendo executado como o programa principal. Em Python, o atributo __name__ de um módulo é uma variável especial que contém o nome do módulo. 
    #Se o módulo estiver sendo executado como o programa principal, o valor de __name__ será "__main__".
    #no caso, o módulo é a myssql.connector
if __name__ == "__main__":
    main()

    #feliz porque esse código deu certoooooo(apenas o item 1 até momento). Vou fazer mais comentários
