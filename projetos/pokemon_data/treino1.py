'''In this project, I wanted to work new libraries(requests and matplotlib).
I thought working with Pokémons data would make it more fun'''
import requests
import matplotlib.pyplot as plt
pokemons_dict={}
pokemons=['pikachu','charizard','snorlax','piplup','squirtle','machamp','totodile','squirtle']
def pokeinfo(nome):
    url=f'https://pokeapi.co/api/v2/pokemon/{nome}'
    resposta=requests.get(url)
    if resposta.status_code==200:
        dados=resposta.json()
        return {
            'nome':dados['name'],
            'peso':dados['weight']
        }
    else:
        print(f"Erro ao encontrar {nome}: código {resposta.status_code}")
        return None
for p in pokemons:
    dados=pokeinfo(p)
    if dados:
        pokemons_dict[dados['nome']]=dados['peso']/10
print(pokemons_dict)
plt.figure(figsize=(10,6))
barras=plt.bar(pokemons_dict.keys(),pokemons_dict.values(),color='red')
plt.title("Gráfico dos pokémons mais pesados")
plt.xlabel("Pokemons")
plt.ylabel('Peso(KG)')
plt.grid(True)
for barra in barras:
    altura=barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, altura + 10,
             f'{altura:.1f}', ha='center', va='bottom', fontsize=10, color='black')
plt.show()
