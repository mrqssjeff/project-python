total = list([[], []])
while True:
    for c in range(1, 8):
        valor = int(input(f'Digite o {c} valor: '))
        if valor % 2 == 0:
            total[0].append(valor)
        if valor % 2 != 0:
            total[1].append(valor)
    total[0].sort()
    total[1].sort()
    print(f'Os valores pares em ordem crescente são {total[0]}')
    print(f'Os valores ímpares em ordem crescente são {total[1]}')
    break
