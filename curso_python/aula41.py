"""while/else"""

string = 'Valor qualquer'
#string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

#Se tiver um "break" no meio do caminho, ele não executa o "else"
    if letra ==' ':
        break

    print(letra)
    i += 1
else:
    print('O "else" foi executado')

print('Aqui já é fora do "while"')