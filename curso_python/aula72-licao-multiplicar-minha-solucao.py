
entrada = ''
entrada_int = 0
entrada_lista = []

def multiplicacao(*args):
    produto = 1
    for numero in args:
        produto = numero * produto
    return numero


entrada = input('Digite os números a ser multiplicados, por favor:')

if entrada.isdigit():
    entrada_int = int(entrada)
    entrada_lista = [entrada_int]
    
    resultado = multiplicacao(entrada_lista)

    print(resultado)


else:
    entrada = input('Ixi, você não digitou somente números, vamos tentar novamente:')