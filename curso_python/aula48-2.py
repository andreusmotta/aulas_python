"""
Listas em Python.
Tipo list - Mutável.
Suporta vários valores de qualquer tipo.
Conhecimentos reutilizáveis - índices e fatiamento.
Métodos úteis: append, insert, pop, del, clear, extend, +

Create Read Update Delete = CRUD
Criar, Ler, Alterar, apagar = lista[i] (CRUD)

"""

#        0   1   2   3 = índices
lista = [10, 20, 30, 40]
# numero = lista[2]
# print(numero)
# lista[2] = 300
# del lista [2]
# print(lista)
# print(lista[2])

# lista.append(50)
# lista.append(60)
# lista.append(70)
# print(lista)

lista.append(50)
lista.pop() #remove o último valor.
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop() #coloca o ultimo valor da list na variável
lista.pop(3) # remove o terceiro item da minha lista.
print(lista)
print(lista, 'Removido,', ultimo_valor)