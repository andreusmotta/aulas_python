"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de
inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

lista_atual = []
opcao = ''

while opcao != 's':

    opcao = input('Selecione uma opção: '
              '[i]nserir [a]pagar [l]istar [s]air: ')

  
    if opcao == 'i':
        item = input('Digite o nome do item a ser adicionado: ')
        lista_atual.append(item)
        print(list(enumerate(lista_atual)))
    

    if opcao == 'a':
        item = input('Digite o código do item a ser removido: ')
        if int(item) < len(lista_atual):
            lista_atual.pop(int(item))
            print(list(enumerate(lista_atual)))
        else:
            print('código de item não encontrado')


    if opcao == 'l':
        if lista_atual == []:
            print('Não há nada em sua lista')
        else:
            print(list(enumerate(lista_atual)))

else:
    print('Boas compras!!!')