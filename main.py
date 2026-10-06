def mostrar_menu():
    print("=== MENU ===")
    print("1 - Ver mensagem")
    print("0 - Sair")

def mostrar_mensagem():
    print('Bem-Vindo!')

def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco = float(input("preco do produto: "))

    print("produto cadastrado com sucesso!")
    
    mostrar_menu()

opcao = input("Escolha: ")

if opcao == "1":
    mostrar_mensagem()
elif opcao == '0':
    print('Encerrando...')
else:
    print('Opção Inválida!')