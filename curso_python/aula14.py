a = 'A'
b = 'B'
c = 1.1
string1 = 'a={} b={} c={:.2f}'
string2 = 'a={0} b={1} c={2:.2f}'
string3 = 'a={nome0} b={nome1} c={nome2:.2f}'
formato1 = string1.format(a, b, c)
formato2 = string2.format(a, b, c)
formato3 = string3.format(
    nome0=a, nome1=b, nome2=c
    )

print(formato1)
print(formato2)
print(formato3)