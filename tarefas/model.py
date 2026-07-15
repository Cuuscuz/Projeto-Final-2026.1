def criar_tarefa(tarefas, descricao): #Função para criar as tarefas
    if len(tarefas) == 0:
        novo_id = 1
    else:
        maior_id = 0
        for tarefa in tarefas:
            if tarefa["id"] > maior_id:
                maior_id = tarefa["id"]
        novo_id = maior_id + 1

    nova_tarefa = {"id": novo_id, "descricao": descricao, "concluida": False}
    tarefas.append(nova_tarefa)
    return nova_tarefa

def buscar_tarefa(tarefas, id_tarefa): #Função que busca as tarefas na lista a partir do ID
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa
    return None

def remover_tarefa(tarefas, id_tarefa): #Função para remover tarefas
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa == None: 
        return False #Se a tarefa não existir (None), não será removida, logo o retorno é False
    tarefas.remove(tarefa)
    return True #Se a tarefa existir, será removida da lista e o retorno será True

def concluir_tarefa(tarefas, id_tarefa): #Função para marcar tarefas concluídas
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa == None:
        return False #Se a tarefa não existir (None), não será concluída, logo o retorno é False
    tarefa["concluida"] = True
    return True #Se a tarefa existir, será marcada como concluída e o retorno será True

def reabrir_tarefa(tarefas, id_tarefa): #Função para reabrir tarefas
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if tarefa == None: #Se a tarefa não existir (None), não será reaberta, logo o retorno é False
        return False
    tarefa["concluida"] = False #Reabre a tarefa
    return True