#Exercicio que adiciona preços em uma lista e depois atualiza com porcentagem de aumento filtrada, utilizando list comprehesion
precos=[]
preco=float(input("Qual valor deseja adicionar ao preço: "))
while preco != 0:
    precos.append(preco)
    preco=float(input("Qual valor deseja adicionar ao preço: "))
print("Os valores são: \n")
print(precos)
aumento=float(input("Defina o aumento percentual: "))
novos_precos=[valor*(1+aumento/100) for valor in precos if valor<100]
for valor in novos_precos:
    print(f"{valor:.2f}")