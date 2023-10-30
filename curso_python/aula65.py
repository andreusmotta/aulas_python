"""
Introdução as funções 9def0 em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para paramentros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print():            # Funções definidas.
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# Print()                 # Precisa abrir e fechar parenteses pra executar a função.



# def imprimir(a, b, c):     # a, b, e c são váriáveis, parâmetros que devem ser preenchidos por argumentos.
#     print(a, b, c)
    
# imprimir(1, 2, 3)
# imprimir(4, 5, 6)



# def saudacao(nome):         # Desse jeito o argumento que eu colocar quando eu chamar a função vai retornar dentro do print quando ele executa a função.
#     print(f'Olá, seja bem vindo, {nome}!')

# saudacao('Andreus')
# saudacao('Thiago')



def saudacao(nome='Sem nome'):# Declarando um valor para o parâmetro antes permite que ele seja mostrado quando não houver nenhum argumento na hora de chamar a função
    print(f'Olá, seja bem vindo, {nome}!')

saudacao()
