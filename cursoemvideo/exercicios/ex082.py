numeros = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        if n % 2 != 0:
            impares.append(n)
    per = ' '
    while per not in 'SN':
        per = str(input('Deseja sair? [S/N]: ')).strip().upper()[0]
    if per == 'S':
        break
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
