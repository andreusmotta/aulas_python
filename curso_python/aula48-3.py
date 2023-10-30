"""
Listas em Python.
Tipo list - Mutável.
Suporta vários valores de qualquer tipo.
Conhecimentos reutilizáveis - índices e fatiamento.
Métodos úteis: append, insert, pop, del, clear, extend, +

Create Read Update Delete = CRUD
Criar, Ler, Alterar, apagar = lista[i] (CRUD)

Métodos úteis:
    append - Adiciona um item ao final.
    insert = Adiciona um item no índice escolhido.
    pop - Remove do final ou do índice escolhido. Também mostra o último item da lista.
    del - Apaga um índice.
    clear - Limpa a lista.
    extend - estende a lista.
    + - Concatena listas.

"""

#        0   1   2   3 = índices
lista = [10, 20, 30, 40]
lista.append('Andreus')
print(lista)
nome = lista.pop()
lista.append(1233)
del lista[-1]
# list.clear()
lista.insert(0, 5) #Primeiro o índice, depois o valor a ser adicionado na posição.
# print(lista[5]) #Dá erro, já que não tem índice na posição 5
lista.insert(100, 5) #Mesmo eu pedindo pra colocar o 5 na posição 100, ele só coloca no final da lista, não na posição 100.
print(lista)