# nome = 'Andreus'
# print(nome[2])
# print(nome[-4])
# print('n' in nome)
# print('N' in nome)
# print('N' not in nome)
# print(10 * '-')

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')