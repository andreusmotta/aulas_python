"""
Valores padrão para parâmetros.
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o o parâmetro, o valor padrão será
usado.
Refatorar: Editar o seu código.
"""

# def soma(x, y):
    # print(x + y)    

# def soma(x, y, z=0):
# def soma(x, y=None, z):     # Assim não funciona porque se eu nomeei um parâmetros, todos os próximos devem ser nomeados.
def soma(x, y, z=None):     # Tanto o Zero quanto o None servem de valor false no booleano.
    # if z:
    if z is not None:       # Desse jeito se eu não colocar um argumento no parâmetro Z, ele vai mandar o "None" que está lá. Se tiver um argumento, ele usa o argumento.
        print(f'{x=} y={y} {z=}', '|', 'x + y + z', x + y + z)
    else:
        print(f'{x=} y={y}', '|', 'x + y', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)