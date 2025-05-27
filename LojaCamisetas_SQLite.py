import sqlite3
import time
def espaco():
    print('=' * 50)
marcas=['Adidas','nike','puma','hering']
tamanhos=['p','m','g']
with sqlite3.connect('camisetas.db') as conexao:
    cursor= conexao.cursor()
    sql='''
    CREATE TABLE IF NOT EXISTS Compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tamanho TEXT NOT NULL,
    data TEXT NOT NULL
    )
    '''
    cursor.execute(sql)
    sql='''
    INSERT INTO Compras(id,nome,tamanho,data)
    values(?,?,?,?)
    '''
    espaco()
    print("Bem vindo(a), estamos com ótimos valores de camisetas, gostaria de realizar uma compra?")
    espaco()
    resp=input('').lower()
    if resp == 'sim':
        espaco()
        print('Tamanhos disponíveis: ')
        print("1-Camisetas tamanho P, por R$35,00 \n 2-Camisetas tamanho m, por R$50,00 \n 3-Camisetas tamanho G, por R$60,00")
        espaco()
        print('As seguintes marcas estão disponiveis: ')
        for x in marcas:
            print(x,end='\n')
        espaco()
        tamanho_op=input("Utilizando o número de cada opção, selecione sua camiseta: ")
        marca=input("Qual marca você deseja: ").capitalize()
        if tamanho_op=='1':
            tamanho='Pequeno'
        elif tamanho_op=='2':
            tamanho='Médio'
        elif tamanho_op == '3':
            tamanho='Grande'
        else: print('Opção inválida'), exit()
        espaco()
        data=time.strftime('%d/%m/%y')
        cursor.execute('''
        INSERT INTO Compras(nome,tamanho,data)
        values(?,?,?)
        ''', (marca,tamanho,data))
        espaco()
        print('Compra registrada com sucesso, parabéns')
        print(f'Marca:{marca} | Tamanho: {tamanho} | Data da compra: {data}')
        espaco()
    else:
        print("Agradecemos a sua atenção")