def salvar_tarefas(tarefas, caminho):
    with open(caminho, 'w') as arq:
        for tarefa in tarefas:
            arq.write(f"{tarefa}\n")
def carregar_tarefas(caminho):
    try:
        with open(caminho) as arq:
            return [linha.strip() for linha in arq.readlines()]
    except FileNotFoundError:
        return []
def add_nova_tarefa(tarefas, tarefa):
    tarefas.append(tarefa)
def listar_tarefas(tarefas):
    for x,y in enumerate(tarefas):
        print(f"{x+1} - {y}")
def concluir(tarefas,indice):
    tarefas.pop(indice-1) if 0 <= indice-1 <= len(tarefas) else ValueError('erro, item da lista não encontrado')

