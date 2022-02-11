s = 0
cont = 0
for c in range(0,6):
    n = int(input('Digite um número qualquer:'))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} números pares e o somatório entre eles é {s}')



