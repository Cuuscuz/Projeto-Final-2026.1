def add_user(usuarios):
    user = str(input("Digite o nome de usuário: "))
    # Deixei somente a variavel user por enquanto, já que o If verifica se o user existe antes de axigir a senha, caso não, ai ele pede a senha.

    if user in usuarios:
        print("Usuário já existente!")

    else:
        senha = str(input("Digite a senha: "))
        usuarios[user] = senha
        # Adicionar usuário usando a função padrão do dicionário.
        print(f"Usuário {user} adicionado!")

def del_user(usuarios):
    user = str(input("Informe o usuário que deseja remover: "))
    if user in usuarios:
        del usuarios[user]
    # Usei a função Del para remover o usuário especifico do dicionário.
        print(f"Usuário {user} deletado!")

    else:
        print("Usuário não encontrado!")

def listar_user(usuarios):
    for user in usuarios:
        print(user)
    # Listar os usuário cadastrados.


# Crio o dicionário para guardar os usuários que posteriormente serão cadastrados.
usuarios = {}

# Escolho o While True para o código em loop, até que o usuário encerre o programa.
while True:
    opc = (input("""
                 
        --USUÁRIOS--
    O que deseja fazer?
    1. Adicionar Usuário...
    2. Remover Usuário.....
    3. Listar Usuários.....
    4. Realizar Login......
    5. Encerrar Programa...
    
    Digite a opção desejada: """))

    if opc == "1":
        add_user(usuarios)

    elif opc == "2":
        del_user(usuarios)

    elif opc == "3":
        listar_user(usuarios)

    elif opc == "5":
        print("Programa encerrado!!!")
        break
        
    elif opc == "4":
        user = str(input("Informe o nome de usuário: "))

        if user in usuarios:
            senha = str(input("Informe a senha do usuário: "))
            if senha == usuarios[user]:
                print("Login realizado com sucesso!")
                
            else:
                print("Senha incorreta!")

        else:
            print("Usuário não encontrado...")
    else:
        print("Opção inválida, selecione uma opção do menu!!!")