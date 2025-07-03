import tarefas
caminho = 'tarefas.txt'
listaDtarefas = tarefas.carregar_tarefas(caminho)
tarefas.salvar_tarefas(listaDtarefas, caminho)
print("Bem vindo ao menu de tarefas")
while True:
    opcao = int(input(
        "\n Escolha qual opção desejar: \n 1 - Listar tarefas     2 - adionar nova tarefa     3 - concluir/remover     4 - sair"))
    if opcao == 1:
        tarefas.listar_tarefas(listaDtarefas)
    elif opcao == 2:
        tarefa = input("Qual tarefa deseja adicionar: ")
        tarefas.add_nova_tarefa(listaDtarefas,tarefa)
    elif opcao == 3:
        remocao=int(input("Qual número da lista deseja remover: "))
        tarefas.concluir(listaDtarefas,remocao)
    elif opcao == 4:
        print("Até logo...")
        tarefas.salvar_tarefas(listaDtarefas, caminho)
        break
print("Fim do programa")