"""
Closure e funções que retornam outras funções.
"""

def criar_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}!'

falar_bom_dia = criar_saudacao('Bom dia', 'Lindo')
falar_boa_noite = criar_saudacao('Boa tarde', 'Fofo')

print(falar_bom_dia, falar_boa_noite)

# ----------------------------------------------

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar()   # Aqui se ficar com os parênteses, ele resolve e entrega o resultado no print lá de baixo.

falar_bom_dia = criar_saudacao('Bom dia', 'Lindo')
falar_boa_noite = criar_saudacao('Boa tarde', 'Fofo')

print(falar_bom_dia)
print(falar_boa_noite)

# ----------------------------------------------

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar   # Agora se tirar os parênteses, ele guarda os resultados na memória, e só entrega o resultado quando fechar os parênteses lá no print.

falar_bom_dia = criar_saudacao('Bom dia', 'Lindo')
falar_boa_noite = criar_saudacao('Boa tarde', 'Fofo')

print(falar_bom_dia())
print(falar_boa_noite())

# ----------------------------------------------

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa tarde')

for nome in ['Andreus', 'Thiago', 'Tiago']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))