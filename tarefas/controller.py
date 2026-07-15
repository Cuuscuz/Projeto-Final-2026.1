from tarefas import view
from tarefas import model

def executar(tarefas):
    while True:
        opcao = view.exibir_menu() #Exibe o menu

        if opcao == "1": #Cria tarefas
            descricao = view.pedir_descricao_tarefa()
            model.criar_tarefa(tarefas, descricao)
            view.exibir_mensagem("Tarefa criada com sucesso!")
        elif opcao == "2": #Exibe a lista de tarefas
            if len(tarefas) == 0:
                view.exibir_mensagem("Lista de tarefas vazia.")
            else:
                view.exibir_tarefas(tarefas)
        elif opcao == "3": #Remove tarefas
            id_tarefa = view.pedir_id_tarefa()
            sucesso = model.remover_tarefa(tarefas, id_tarefa)
            if sucesso:
                view.exibir_mensagem("Tarefa removida com sucesso.")
            else:
                view.exibir_mensagem("Tarefa não encontrada.")
        elif opcao == "4": #Marca tarefas como concluídas
            id_tarefa = view.pedir_id_tarefa()
            sucesso = model.concluir_tarefa(tarefas, id_tarefa)
            if sucesso:
                view.exibir_mensagem("Tarefa concluída com sucesso.")
            else:
                view.exibir_mensagem("Tarefa não encontrada.")
        elif opcao == "5": #Reabre tarefas (retorna ao status de Pendente)
            id_tarefa = view.pedir_id_tarefa()
            sucesso = model.reabrir_tarefa(tarefas, id_tarefa)
            if sucesso:
                view.exibir_mensagem("Tarefa reaberta.")
            else:
                view.exibir_mensagem("Tarefa não encontrada.")
        elif opcao == "6": #Fecha o programa.
            break
        else:
            view.exibir_mensagem("Opção inválida!")