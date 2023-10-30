
# texto = 'Python s2'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)

#     i +=1

#-----------------------------------------------

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x):')

#     repeticoes += 1

# print(f'Você digitou a senha errada {repeticoes} vezes.')
# # print('Você digitou a senha errada',repeticoes,'vezes.')
# print('Aquele laço acima pode ter repetições infinitas')

#-----------------------------------------------

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')