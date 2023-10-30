"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = input('Digite um número inteiro, por favor: ')

try:
    1 % int(numero_digitado)
    
    if (int(numero_digitado) % 2 == 0) == True:
        print(f'O número digitado {numero_digitado} é PAR')
    
    else:
        print(f'O número digitado {numero_digitado} é IMPAR')

except:
    print('Não foi digitado um número inteiro.')

# solução do professor:

"""
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
"""