from usuarios import model
from usuarios import view
from tarefas import controller

# Controla o cadastro de usuários
def adicionar():

    # solicita o nome do usuário através da View.
    nome = view.pedir_usuario()

    # Verifica se o usuário já existe.
    if nome in model.usuarios:
        view.mostrar("Usuário já existente!")
        return

    # Pede a senha so se o usuario não existir
    senha = view.pedir_senha()

    # Solicita ao Model que cadastre o usuário.
    if model.adicionar_usuario(nome, senha):
        view.mostrar(f"Usuário {nome} adicionado!")


# Controla a remoção dos usuários.
def remover():

    nome = view.pedir_usuario_remover()

    if model.remover_usuario(nome):
        view.mostrar(f"Usuário {nome} deletado!")

    else:
        view.mostrar("Usuário não encontrado!")


# Controla a lista dos usuários que já tão cadastrados
def listar():

    usuarios = model.listar_usuarios()

    view.listar(usuarios)


# Controla o login indo para a parte do Yuri (:
def login():

    # Solicita o nome do usuário.
    nome = view.pedir_usuario()

    # Solicita a senha.
    senha = view.pedir_senha()

    # Solicita ao Model que verifique se o login é válido
    if model.login(nome, senha):

        view.mostrar("Login realizado com sucesso!")

        # Cria a lista de tarefas e chama o Controller das tarefas (função do Yuri)
        tarefas = []

        controller.executar(tarefas)

    else:
        view.mostrar("Usuário ou senha incorretos!")