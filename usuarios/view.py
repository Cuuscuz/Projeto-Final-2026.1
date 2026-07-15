
# Mostra o menu principal e retorna a opção que o usua´rio escolheu
def menu():
    return input("""
        --USUÁRIOS--
    O que deseja fazer?
    1. Adicionar Usuário...
    2. Remover Usuário.....
    3. Listar Usuários.....
    4. Realizar Login......
    5. Encerrar Programa...

Digite a opção desejada: """)


# Solicita ao usuário o nome de usuaario.
def pedir_usuario():
    return input("Digite o nome de usuário: ")


# Solicita a senha.
def pedir_senha():
    return input("Digite a senha: ")


# Solicita qual usuário será removido
def pedir_usuario_remover():
    return input("Informe o usuário que deseja remover: ")


# Exibe qualquer mensagem para o usuário.
def mostrar(msg):
    print(msg)


# lista todos os usuarios cadastrados.
def listar(usuarios):

    if len(usuarios) == 0:
        print("Lista de usuários vazia...")

    else:
        for usuario in usuarios:
            print(usuario)