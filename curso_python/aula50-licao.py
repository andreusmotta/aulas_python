"""
Exercício: Exiba os índices da lista:
0 - Andreus
1 - Fulano
2 - Siclano
3 - Beltrano
"""
lista = ['Andreus', 'Fulano', 'Siclano', 'Beltrano']
total_na_lista = len(lista)
item_na_lista = range(total_na_lista)
lista_completa = []
i = 0

while i < total_na_lista:
    lista_completa.insert(i, (int(i), lista[i]))
    i += 1

for nome in lista_completa:
    print(nome)

"""
Solução do professor:

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

"""