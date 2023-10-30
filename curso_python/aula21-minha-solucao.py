entrada = input('[E]ntrar [S]air ')
## senha_digitada = input('Senha: ')
senha_permitida = '123456'


if entrada == 'S':
    print('Sair')
elif entrada == 'E':
    senha_digitada = input('Senha: ')
    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrar')
    else:
        print('Sair')    
else:
    print('Sair')