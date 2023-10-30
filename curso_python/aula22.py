entrada = input('[E]ntrar' '[S]air')
senha_digitada = input ('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada:
    print('Entrar')
else:
    print('Sair')

# Avaliação Curto Circuíto

# print(True and 0 and True)

# print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)