"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '    Olha só que     ,     coisa interessantes              '
# lista_frases = frase.split(',')
lista_frases_cruas = frase.split(',')
print(lista_frases_cruas)
# for i, frase in enumerate(lista_frases):
#     # print(lista_frases[i])
#     print(lista_frases[i].strip()) # O strip corta os espaços do COMEÇO e do FIM somente, os do meio ficam.
#     print(lista_frases[i].rstrip()) # Tira os espaços do direta (ou do fim)
#     print(lista_frases[i].lstrip()) # Tira os espaços da esquerda (ou do começo)

# for i, frase in enumerate(lista_frases):
#     print(lista_frases)
#     print(i)
#     lista_frases[i] = lista_frases[i].strip()

lista_frases_arrumadas = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases_arrumadas.append(lista_frases_cruas[i].strip())
    print(lista_frases_arrumadas)
# print(lista_frases_cruas) 
# print(lista_frases_arrumadas)

# frases_unidas = '-'.join('abc') # O join coloca caracteres entre os iteráveis
# frases_unidas = '-'.join(lista_frases_arrumadas) # vai dar "Olha só que-coisa interessantes".
frases_unidas = ', '.join(lista_frases_arrumadas)
print(frases_unidas)