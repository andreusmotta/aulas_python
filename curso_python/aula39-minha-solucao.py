# nome = 'Andreus Pereira' #strings são iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

#Andreus Pereira tem 15 letras
# nome = 'Andreus Pereira' #strings são iteráveis
# contador = 0
# # contador_len = 0

# while contador <= 15:
#     # contador += 1
#     # print(contador)
    
#     # print(f'*{nome[contador]}') * 15
#     print('*', nome[contador]) * 15
#     contador += 1

#     # if contador == 8:
#     #     continue

#     if contador == 15:
#         break

#Solução do professor:

nome = 'Andreus Pereira' #strings são iteráveis
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    # novo_nome += letra
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
