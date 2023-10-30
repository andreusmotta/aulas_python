"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_captada = input('Que horas são agora por favor? ')
hora = float(hora_captada)
manha = hora <= 11.59
tarde = (hora >= 12.00) and hora <= 17.59

if hora < 24.01:

    if manha:
        print('Bom dia.')

    elif tarde:
        print('Boa tarde.')

    else:
        print('Boa noite.')
else:
    print('Horário inválido')

#Solução do professor:
"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""