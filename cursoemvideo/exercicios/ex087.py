matriz = list([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
somapar = maior = somater = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para a posição |{i}, {j}|: '))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^5}', end='')
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            somater += matriz[i][j]
    print()
print(f'A soma dos pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somater}')
for j in range(0, 3):
    if j == 0:
        maior = matriz[1][j]
    elif matriz[1][j] > maior:
        maior = matriz[1][j]
print(f'O maior valor da segunda linha é {maior}')

