nome = 'Andreus Pereira'
altura = 1.77
peso = 135
# imc = ... #IMC = peso / (altura x altura)
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'Pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

# print(nome, 'tem', altura,'de altura,', 'pesa', peso, 'quilos e seu IMC é', imc)

print(linha_1)
print(linha_2, linha_3)
# print(linha_3)