"""
Argumentos nomeados e não nomeados em funções Python.
Argumento nomeado tem nome com sinal de igual.
rgumento não nomeador recebe apenas o argumento (valor).
"""

# Definição da função
# def soma(x, y):
#     # Definição
#     # print(x + y)
#     print(f'{x=} y={y}', '|', 'x + y', x + y) # O {x=} é a mesma coisa que o y={y}, eles imprimem igual.

# # print(soma)     # Imprime somente o nome da função e a posição na memória.

# # print(soma(1, 2)) # Imprime a soma e None, porque a soma é o que tá no print da função, e print de função depois retorna None.

# soma(1, 2)
# soma(2, 1)
# soma(y=2, x=1) #Assim é pra quando ce quer um argumento nomeado, aí tem que indicar os parãmetros que receberão os argumentos.

...


def soma(x, y, z):
     print(f'{x=} y={y} {z=}', '|', 'x + y + z', x + y + z)

soma(1, 2, 3)
soma(y=2, z=3, x=1)
# soma(1, 2, z=5)     # Assim funciona também, ele vai pegar os argumentos na ordem dos parâmetros até chegar o valor nomeado. 
# soma(1, y=2, 5)     # Assim não funciona. Após um argumento nomeado, todos os seguintes devem ser argumentos nomeados.

print(1, 2, 3, sep='-') # O sep permite escolher um caractere separador na hora de mostrar os argumentos.