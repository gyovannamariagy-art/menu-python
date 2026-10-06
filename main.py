def mostrar_menu():
    print("=== MENU ===")
    print("1 - Ver mensagem")
    print("0 - Sair")

def mostrar_mensagem():
    print('Bem-Vindo!')

    mostrar_menu()

opcao = input("Escolha: ")

if opcao == "1":
    mostrar_mensagem()
elif opcao == '0':
    print('Encerrando...')
else:
    print('Opção Inválida!')