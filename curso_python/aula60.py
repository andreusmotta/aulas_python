"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

# print('Valor' if True else 'Outro valor')
# print('Valor' if False else 'Outro valor')

# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

# digito = 9

# novo_digito = digito if digito <= 9 else 0
# # novo_digito = 0 if digito > 9 else digito

# print(novo_digito)

print('Valor' if True else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if False else 'Fim')