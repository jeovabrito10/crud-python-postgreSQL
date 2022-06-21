from programa import listar, inserir, atualizar, deletar


def menu():


    print("==========Gerenciamneto de Servidores==========")
    print("Selecione uma opção: ")
    print("1 - Listar Servidor")
    print("2 - Inserir Servidor")
    print("3 - Atualizar Servidor")
    print("4 - Deletar Servidor")
    opcao = int(input("Ecolha uma Opçao: "))
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print("Opção Inválida!")
    else:
        print("Opção Inválida!")


if __name__ == '__main__':
    menu()
