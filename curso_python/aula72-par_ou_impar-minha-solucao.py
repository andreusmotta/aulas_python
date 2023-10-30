"""
Fazer uma função que retorne se um número é par ou impar.
"""

entrada = ''


def verificador(x):
    if x % 2 == 0:
        print(f"O número {x} é par")
    else:
        print(f"O número {x} é impar")


entrada = input('Por favor, digite um número bem legal: ')

resultado = verificador(int(entrada))

# print(resultado)
