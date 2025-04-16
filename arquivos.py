print("Inicio do programa")
estoque={}
with open('pratica.txt','r') as arq:
    linhas=arq.readlines()
    for linha in linhas:
        lst=linha.rstrip().split(';')#split separa as palavras atra´ves dos espaços e retorna com uma lista, onde cada palavra é um elemento
        cod=int(lst[0])
        qtd=int(lst[1])
        pcunit=float(lst[2])
        estoque[cod]=(qtd,  pcunit)
print('Valores carregados no dicionário')
print(estoque)
print('Exibição dos dados em forma de tabela')
TotGeral=0
for cod, dados in estoque.items():
    TotGeral= dados[0]*dados[1]
    print(f'{cod}: {dados[0]:5d} x {dados[1]:6.2f} = {dados[0]*dados[1]:8.2f}')
print(' '* 24, f'TOTAL GERAL: {TotGeral:8.2f}')