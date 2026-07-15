
# crio o dicionário para guardar os usuários cadastrados.
usuarios = {}

def adicionar_usuario(nome, senha):
    # Verifica se o usuário já existe.
    if nome in usuarios:
        return False

    # Adiciona o usuário ao dicionário utilizndo o nome como chave
    # e a senha como valor.
    usuarios[nome] = senha
    return True

def remover_usuario(nome):
    # Verifica se o usuario existe antes de remover.
    if nome in usuarios:
        # Remove o usuário utilizando a função padrão del
        del usuarios[nome]
        return True

    return False

def listar_usuarios():
    # Retorna todo o dicionario de usuários.
    return usuarios

def login(nome, senha):
    # Verifica se o usuário existe e se a senha informada
    # é igual a senha cadastrada.
    if nome in usuarios and usuarios[nome] == senha:
        return True

    return False