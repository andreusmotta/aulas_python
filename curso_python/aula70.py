"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    # print(x, y)     # Com o print, não retorna valor nenhum, ele só serve pra mostrar coisas na tela, então mostrar na tela no final do código não rola.
    # return x + y    # O return sim "retorna" valores, aí da pra adicionar eles nas variáveis e tal. Não pode colocar mais nada depois do return, ele "acaba" a função.
    if x > 10:
        return [10, 20] # Não precisa colocar o else depois, porque o return pára toda a função.
    return x + y


# variavel = print('Andreus')
# print(variavel)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
# print(soma1 + soma2)
print(soma1)
print(soma2)
print(soma(11, 55))