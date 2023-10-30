"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
#            746.824.890-70
cpf_teste = '746.824.890-70'
cpf_entrada = ''
cpf_lista = []
caractere = ''
caractere_int = 0
lista_produto = []
soma = 0
produto = 0
resto = 0
digito_1 = 0
digito_2 = 0

cpf_entrada = input('Bom dia, amigo! Por favor digite o seu CPFzim no formatim 123.456.789-10: ')
# testar a quantidade de caracteres, remover os pontos e traços, e ver se é tudo número.
while True:
    
    if len(cpf_entrada) == 14: # Testa se a entrada tem tamanho de CPF.
        cpf_lista = [*cpf_entrada]
        cpf_lista.pop(13)
        cpf_lista.pop(12)
        cpf_lista.pop(11)

        for i, caractere in enumerate(cpf_lista): # Retira os caracteres não números da lista.
            try:
                caractere_int = int(caractere)
            except:
                cpf_lista.pop(i)

        m = 10
        for caractere in cpf_lista: # Multiplica os caracteres por 10, 9, 8...
            caractere_int = int(caractere)
            lista_produto.append(m * caractere_int)
            m = m - 1
            
        print(f"A lista com os 10 valores multiplicados é {lista_produto}")

        for caractere in lista_produto: # Soma os caracteres dentro da lista e joga na variavel "soma"
            soma = soma + caractere
            
        print(f"A soma final dos 10 itens é {soma}")

        produto = 10 * soma # Multiplicar por 10, pede na questão
        print(f"O produto da multiplicação é {produto}")

        resto = produto % 11 # Quarda o resto da divisão por 11 na variável "resto"
        print(f"O resto da divisão é {resto}")

        if resto < 9:
            digito_1 = resto                     
        else:
            digito_1 = 0
        
        print(f"O primeiro dígito do seu lindo CPF é {digito_1}")
      
        # -----------------------------------------
      
        cpf_lista.append(digito_1)

        # Limpando as variáveis usadas antes pra aproveitar o código
        lista_produto = []
        soma = 0

        m = 11
        for caractere in cpf_lista: # Multiplica os caracteres por 10, 9, 8...
            caractere_int = int(caractere)
            lista_produto.append(m * caractere_int)
            m = m - 1
            
        print(f"A lista com os 11 valores multiplicados é {lista_produto}")

        for caractere in lista_produto: # Soma os caracteres dentro da lista e joga na variavel "soma"
            soma = soma + caractere
                        
        print(f"A soma final dos 11 itens é {soma}")

        produto = 10 * soma # Multiplicar por 10, pede na questão
        print(f"O novo produto da multiplicação é {produto}")

        resto = produto % 11 # Quarda o resto da divisão por 11 na variável "resto"
        print(f"O resto da divisão é {resto}")

        if resto < 9:
            digito_2 = resto                     
        else:
            digito_2 = 0
        
        print(f"O segundo dígito do seu lindo CPF é {digito_2}")

        print(f'Os dígitos do seu cpf massa são: {digito_1}{digito_2}')

        break

    cpf_entrada = input('Eita algo deu errado =( Poderia digitar novamente o CPF? ')
