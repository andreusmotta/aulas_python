"""
Iterável -> str, tange, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez.
next -> me entregue o próximo valor.
iter -> me entregue seu iterador.
"""

# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)

#---------------------------------------------------------

# texto = iter('Andreus') #'Andreus'.__iter__

# # print(texto)
# print(next(texto)) #(texto.__next__())
# print(next(texto)) #(texto.__next__())
# print(next(texto)) #(texto.__next__())
# print(next(texto)) #(texto.__next__())
# print(next(texto)) #(texto.__next__())
# print(next(texto)) #(texto.__next__())
# print(next(texto)) #(texto.__next__())

#---------------------------------------------------------

# texto = 'Andreus' # Iterável
# iterador = iter(texto) # Iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
        # break

# Ou usar o For pra fazer o mesmo que acima:

texto = 'Andreus'

for letra in texto:
    print(letra)