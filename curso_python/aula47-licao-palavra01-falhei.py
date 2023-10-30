"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'Jared'
tentativas = 0
resposta = '*****'
letra = ''
indice = 0


while resposta != palavra_secreta:
    letra = input('Digite uma letra: ')
    if letra == 'J':
        resposta[0] = letra
        print(resposta)
    elif letra == 'a':
        resposta[1] = letra
        print(resposta)
    elif letra == 'r':
        resposta[2] = letra
        print(resposta)
    elif letra == 'e':
        resposta[3] = letra
        print(resposta)
    elif letra == 'd':
        resposta[4] = letra
        print(resposta)
    else:
        print(resposta)


else:
    print('Ae caralho, cê acertou!!!')
    print('Ah meu, a palavra era "Jared", né? O que você esperava?')
    print(f'Foram {tentativas} tentativas.')
