n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}!')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ' f'{f}', end='')
    f *= c
    c -= 1
