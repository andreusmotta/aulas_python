"""Desempacotamento em chamadas
de métodos e funcões
"""
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena', ], 
    ['Elaine', ], 
    ['Luiz', 'João', 'Eduardo', ], 
]
# a, b, c, *_ = lista
# print(a, c) # Mostra 'Maria 1".

# p, b, *_, ap, u = lista 
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ', sep=' ') #Isso é a mesma coisa que isso: print(*lista)

print(*lista)
print(*string)
print(*tupla)

# print(*salas, end='\n')
print(*salas, sep='\n')