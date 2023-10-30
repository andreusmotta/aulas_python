"""
Lista de listas e seus índices
"""

salas = [
    # 0         1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0         1       2           3
    ['Luiz', 'João', 'Eduarda', (10,20,30,40,50), ], # 2
]

# print(salas[1][0]) # Vai mostrar o valor "Elaine"
# print(salas[0][1]) # Vai mostrar o valor "Helena"
# print(salas[2][2]) # Vai mostrar o valor "Eduarda"
# print(salas[2][3][3]) # Vai mostrar o valor "40"

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)