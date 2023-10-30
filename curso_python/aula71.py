"""
args - Argumentos não nomeados.
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4       # O 1 foi pro x, o 2 foi pro y e o 3 e o 4 foram adicionados na *resto como uma tupla.
print(x, y, resto)


# def soma(x, y):
#     return x + y

# print(1, 2, 3, 4, 5)

# def soma(*args):              # O *args permite adicionar qualquer coisa do jeito que estiver nele, geralmente como uma tupla, que não são alteráveis
    # args = list(args)       # Também da pra falar que o args (dentro da função) será uma lista, aí ele coloca como lista, que dá pra modificar o conteúdo.
    # print(args, type(args))
    # total = 0
    # for numero in args:
    #     print('Total', total, numero)
    #     total += numero        # Isso é a mesma coisa que: total = total + numero
    #     print('Total', total)
    # print(total)

# soma(1, 2, 3, 4, 5, 6)

def soma(*args):        # Toda essa função pode ser resumida a função do Python "sum()", de soma.
    total = 0
    for numero in args:
        total += numero        # Isso é a mesma coisa que: total = total + numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_1_2_3)

outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 78, 10)
print(outra_soma)

