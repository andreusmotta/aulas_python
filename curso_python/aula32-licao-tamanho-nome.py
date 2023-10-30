"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_entrada = input('Digite o seu nome, por favor: ')

nome = len(nome_entrada)

if nome <= 4:
    print(f'O seu nome {nome_entrada} é muito pequeno')

elif nome >= 5 and nome <= 6:
    print(f'O seu nome {nome_entrada} é de tamanho normal')

else:
    print(f'O seu nome {nome_entrada} é muito grande.')

#Solução do professor:

"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
"""