s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0 and c % 2 == 1:
        s += c
        cont += 1
print(f'A  soma de {cont} valores múltiplos de 3 entre 1 e 501 é {s}')
