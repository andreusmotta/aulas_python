"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
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

cpf_entrada = input('Bom dia, amigo! Por favor digite o seu CPFzim: ')
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
            
        print(f"A lista com os valores multiplicados é {lista_produto}")

        for caractere in lista_produto: # Soma os caracteres dentro da lista e joga na variavel "soma"
            soma = soma + caractere
            
        print(f"A soma final dos itens é {soma}")

        produto = 10 * soma # Multiplicar por 10, pede na questão
        print(f"O produto da multiplicação é {produto}")

        resto = produto % 11 # Quarda o resto da divisão por 11 na variável "resto"
        print(f"O resto da divisão é {resto}")

        if resto < 9:
            print(f"O primeiro dígito verificador do seu lindo CPF é {resto}")
            break
        else:
            print("O primeiro dígito verificador do seu lindo CPF é 0(zero)")
            break

    cpf_entrada = input('Eita algo deu errado =( Poderia digitar novamente o CPF? ')
"""
25/04/2023 - Consegui finalmente separar cada caracter em um iterável de uma lista, agora preciso remover os pontos e traços.
26/04/2023 - Consegui tirar todos os caracteres estranhos e deixar só os números, agora preciso multiplicar os trens
26/04/2023 - Consegui multiplicar os trens. Agora tenho que somar eles.
26/04/2023 - Consegui somar eles, agora sei lá o que tem que fazer. Ah tem que achar o resto de uma divisão por 11.
26/04/2023 - Consegui carajo!!!
27/04/2023 - Esqueci de multiplicar por 10 depois de somar, masquenhaca
"""