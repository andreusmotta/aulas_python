#Imutáveis: str, int, float, bool

string = 'Andreus'
string_minuscula = 'andreus'
# outra_variavel = string
outra_variavel = f'{string[:3]}ABC{string[4:]}'
string_1000 = '1000'
# string[3] = 'ABC'
# print(string[3])
print(string)
print(outra_variavel)
print(string_minuscula)
print(string_minuscula.capitalize())
print(string.zfill(100))
print(string_1000.zfill(10))