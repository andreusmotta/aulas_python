"""
Higher Order Functions
Funções de Primeira Classe
"""


"""
def saudacao(msg): # Passo 3 = Essa função recebeu de parâmetro o "Bom dia", e vai retornar ele na variável "v" lá em baixo.
    return msg 

def executa(funcao, texto):
    return funcao(texto) # Passo 2 = Essa função retornou dentro do parametro "funcao" a funcão "saudacao", ficando tipo "saudacao(Bom dia)""

v = executa(saudacao, 'Bom dia') # Passo 1 = Os parâmetros da função "executa" são a função "saudação" e o "Bom dia".

print(v) # Passo 4 = Depois dessa volta toda, imprime o "Bom dia".
"""

def saudacao(msg, nome): 
    return f'{msg}, {nome}!' # Passo 4 = a função "saudacao" recebe a tupla como seus dois argumentos e retorna eles dentro da mensagem
                             #formatada, que sera colocada na variável 'v'.

def executa(funcao, *args): # Passo 2 = O primeiro parâmetro recebe a funcão "saudacao" e o args recebe a tupla 'Bom dia', 'meu amor'
    return funcao(*args) # Passo 3 = Aqui o args é desempacotado e atupla entra na função como argumentos, ficando o retorno "saudacao('Bom dia', 'meu amor')"

v = executa(saudacao, 'Bom dia', 'meu amor') #  Passo 1 = Agora estou jogando três parâmetros na função "executa", dois deles numa tupla empacotada no *args.

print(v)

print(
    executa(saudacao, 'Bom dia', 'meu amor')
)

print(
    executa(saudacao, 'Bom dia', 'docinho')
)