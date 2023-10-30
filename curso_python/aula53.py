"""
enumerate - enumera iteráveis (índices)
"""

# Solução do professor:

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)
# lista_enumerada - list(enumerate(lista)) # Assim ele transforma o que ele "enumerou" em uma lista mutável.
# print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)