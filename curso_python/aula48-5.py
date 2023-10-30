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
# nome = 'Andreus'
# nome = 'Fulano'
# print(nome)

# nome = 'Andreus'
# noutra_variavel = nome
# nome = 'Fulano'
# print(nome)
# print(noutra_variavel)

# lista_a = ['Andreus', 'Fulano']
# lista_b = lista_a
# print(lista_b)

# lista_a = ['Andreus', 'Fulano']
# lista_b = lista_a #fazer isso não "grava" o conteúdo da lista_a na lista_b, ele "liga" as duas listas tipo como um hardlink. Se muda algo em uma lista, muda na outra.
# lista_a[0] = 'Siclano'
# print(lista_b) #vai aparecer o Siclano no lugar do Andreus porque as duas listas estão interligadas e alinha anterior trocou o valor do índice 0.

lista_a = ['Andreus', 'Fulano']
lista_b = lista_a.copy() #Usando o método "copy()" você consegue de verdade copiar o valor da lista_a para a lista_b.

lista_a[0] = 'Siclano'
print(lista_b) 
print(lista_a)