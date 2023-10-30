"""
Repetições
while (enquanto)
Executa uma condição enquanto ela for veradeira.
Loop infinito -> Quando um código não tem fim.
"""

condicao = True

while condicao:
    nome = input('Qual é o seu nome, por favor? ')
    print(f'O seu nome é {nome}')
    #O Break "quebra" o while onde ele está dentro.
    # break
    if nome =='sair':
        break
print('Terminamos, muito obrigado!!!')