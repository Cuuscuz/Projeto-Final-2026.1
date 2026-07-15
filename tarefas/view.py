def exibir_mensagem(msg): #Exibe qualquer mensagem de aviso, sucesso ou erro
    print(msg)

def exibir_tarefas(tarefas): #Exibe todos os dados da tarefa: ID, descrição e o status (Pendente/Concluída)
    for tarefa in tarefas:
        if tarefa["concluida"]:
            status = "Concluída"
        else:
            status = "Pendente"
        print(tarefa["id"], "-", tarefa["descricao"], "-", status)

def pedir_descricao_tarefa(): #Recebe a descricao da tarefa
    descricao = input("Descreva sua tarefa: ")
    return descricao

def pedir_id_tarefa(): #Recebe o ID da tarefa
    id_tarefa = int(input("Digite o ID da sua tarefa: "))
    return id_tarefa

def exibir_menu(): #Exibe o menu
    print("""
1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Concluir tarefa
5 - Reabrir tarefa
6 - Sair
""")
    opcao = input("Digite uma opção: ")
    return opcao