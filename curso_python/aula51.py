"""
Introdução ao desempacotamento + tuplas.
"""

nomes = ['Andreus', 'Fulano', 'Siclano']
nome1, nome2, nome3 = nomes

# Pode ser assim também:
# nome1, nome2, nome3 = ['Andreus', 'Fulano', 'Siclano']

nome1, *resto = ['Andreus', 'Fulano', 'Siclano'] # A variável de resto pegga todos os outros dados empacotados na lista.

_, _, nome, *_ = ['Andreus', 'Fulano', 'Siclano'] # O Underline é uma variável que fala pra quem lê que você não usa essa variável, mas precisa dela.

print(nome1, resto)