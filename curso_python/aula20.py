primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

int_valor1 = int(primeiro_valor)
int_valor2 = int(segundo_valor)

if int_valor1 > int_valor2:
    print(int_valor1, 'é maior do que o segundo valor ', int_valor2)
else:
    print(int_valor2, 'é maior do que o primeiro valor ', int_valor1)
