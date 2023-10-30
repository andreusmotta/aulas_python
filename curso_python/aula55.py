"""
Imprecisão de Ponto flutuante
Double-precision floating-point format IEEE 754
---Links pra pegar na aula---
"""

# Maneiras de resolver os problemas dos pontos flutuantes não serem precisos:
# numero_1 = 0.1
# numero_2 = 0.7
# numero_3 = numero_1 + numero_2
# print(numero_3)
# print(f'{numero_3:.2f}')
# print(round(numero_3, 3)) # O segundo número é a quantidade de casas depois da vírgula, mas se estiverarredondado pra zero, ele não mostra.
# print(round(numero_3, 10))

# Ou usar o "decimal"

import decimal

# numero_1 = decimal.Decimal(0.1)
# numero_2 = decimal.Decimal(0.7)
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)