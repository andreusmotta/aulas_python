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

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b
# print(lista_c)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) #Assim ele não retorna valor, ele só modifica a lista_a. Então botar numa variável não rola, por exemplo: "lista_d = lista_a.extend(lista_b)". Isso não retorna valor
print(lista_a)