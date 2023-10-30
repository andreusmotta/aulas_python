"""
Tipo tupla - Uma lista imutável.
"""

# _, _, nome, *_ = ['Andreus', 'Fulano', 'Siclano']

nomes = ['Andreus', 'Fulano', 'Siclano']
nomes = tuple(nomes) # Tuplas podem ser convertidas para listas e vice versa. Tuplas são imutáveis, não da pra alterar um valor em uma posição igual nas listas.
nomes = list(nomes)
print(nomes[-1])
print(nomes)