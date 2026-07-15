from usuarios import controller
from usuarios import view

# Escolho o While True para o código em loop,
# até que o usuário encerre o programa.
while True:

    opc = view.menu()

    if opc == "1":
        controller.adicionar()

    elif opc == "2":
        controller.remover()

    elif opc == "3":
        controller.listar()

    elif opc == "4":
        controller.login()

    elif opc == "5":
        print("Programa encerrado!!!")
        break

    else:
        print("Opção inválida, selecione uma opção do menu!!!")