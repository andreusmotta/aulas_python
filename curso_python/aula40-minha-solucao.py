"""Calculadora com while"""

primeiro_numero = ''
segundo_numero = ''
operador = input('Olá, você gostaria de calcular? Escolha uma das opções: 1 para somar, 2 para subtrair,'
                 '3 para multiplicar, 4 para dividir ou 5 para sair. Digite somente o número da sua escolha, por favor: ')

while '5' not in operador: #Aqui eu queria que fosse só o 5, e não qualquer cinco no meio de qualquer tranqueira digitada, comofas?
    while operador == '1' or operador == '2' or operador == '3' or operador == '4':
        
        if operador == '1':
            try:
                primeiro_numero = float(input('Oba, vamos somar!!! Por favor, digite o primeiro número: '))
                segundo_numero = float(input('Massa, agora mande o segundo número: '))
                print(f'O resultado da sua soma é, tcharammm: {primeiro_numero + segundo_numero}')
                break
            except:
                print('Não véi, tem que digitar números =*(')
                continue

        if operador == '2':
            try:
                primeiro_numero = float(input('Ae, vamos fazer continha de menos!!! Por favor, digite o primeiro número: '))
                segundo_numero = float(input('Massa, agora mande o segundo número: '))
                print(f'O resultado da sua continha é, tcharammm: {primeiro_numero - segundo_numero}')
                break
            except:
                print('Não véi, tem que digitar números =*(')
                continue

        if operador == '3':
            try:
                primeiro_numero = float(input('Uhulll, vamos multiplicar o pão!!! Por favor, digite o primeiro número: '))
                segundo_numero = float(input('Massa, agora mande o segundo número: '))
                print(f'O resultado da sua graça concedia é, tcharammm: {primeiro_numero * segundo_numero}')
                break
            except:
                print('Não véi, tem que digitar números =*(')
                continue

        if operador == '4':
            try:
                primeiro_numero = float(input('Ae koroi, dividir para conquistar!!! Por favor, digite o primeiro número: '))
                segundo_numero = float(input('Massa, agora mande o segundo número: '))
                print(f'O resultado da sua conquista é, tcharammm: {primeiro_numero / segundo_numero}')
                break
            except:
                print('Não véi, tem que digitar números =*(')
                continue

    operador = input('Opa, vamos mais uma vez!!! Escolha uma das opções: 1 para somar, 2 para subtrair, 3 para multiplicar, 4 para dividir ou 5 para sair, por favor: ')
        
print('Valeu véi, obrigadão!!!')