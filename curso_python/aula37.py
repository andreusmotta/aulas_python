

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('Escondi o número 6')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Tô escondendo o {contador}')
        continue

    print(contador)

    if contador == 40:
        print(contador)
        break

print('Acabou')