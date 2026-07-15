
def add_user(usuarios): # Função de adicionar usuários.
    user = str(input("Digite o nome de usuário: "))
    # Deixei somente a variavel user por enquanto, já que o If verifica se o user existe antes de axigir a senha, caso não, ai ele pede a senha.

    if user in usuarios:
        print("Usuário já existente!")

    else:
        senha = str(input("Digite a senha: "))
        usuarios[user] = senha
        # Adicionar usuário usando a função padrão do dicionário.
        print(f"Usuário {user} adicionado!")

def del_user(usuarios): # Função para deletar usuarios
    user = str(input("Informe o usuário que deseja remover: "))
    if user in usuarios:
        del usuarios[user]
    # Usei a função Del para remover o usuário especifico do dicionário.
        print(f"Usuário {user} deletado!")

    else:
        print("Usuário não encontrado!")

def listar_user(usuarios): # Função para Listar usuários.
    if len(usuarios) == 0:
        print("Lista de usuários vazia...")

    else:
        for user in usuarios:
            print(user)
    # Listar os usuário cadastrados.

def login_user(usuarios): # Função para realizar o login de usuário.
    user = str(input("Informe o nome de usuário: "))

    if user in usuarios:
        senha = str(input("Informe a senha do usuário: "))
        if senha == usuarios[user]:
            print("Login realizado com sucesso!")

            while True:
                tarefas = []
                controller.executar(tarefas)
                break

        else:
            print("Senha incorreta!")

    else:
        print("Usuário não encontrado...")