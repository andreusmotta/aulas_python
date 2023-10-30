"""
Escopo de funções em Python.
Escopo significa o lcoal onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def escopo():
    global x        
    x = 10          # Aqui a variável de mesmo nome que a global é DIFERENTE da variável global e você pode fazer isso. Ela é válida somente dentro da função e das funções
                    # que estão dentro dela.
    def outra_funcao():
        global x    # Dessa maneira dentro da função a variável x terá o valor global dela dentro da função.
        x = 11
        y = 2       # A variavel definida dentro da função é dela somente, a função de fora não consegue usar ela. Mas a variável global é válida dentro das funções tudo.
        print(x, y)
    # x = 1         # A variável está definida dentro da função, então da pra usar ela. Se não estivesse definida aqui, ela DEVE ser definida fora ANTES de chamar a função.
    outra_funcao()
    print(x)

# print(x)          # Como está fora da função, ele fala que não está definido.
print(x)
escopo()
print(x)