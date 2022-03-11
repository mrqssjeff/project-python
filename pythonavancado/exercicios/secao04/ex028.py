soma = e = 0
for c in range(0, 3):
    num = float(input(f'Digite o {c+1}° valor: '))
    e = num ** 2
    soma += e
print(f'O valor do somatório da soma dos quadrados dos três valores é {soma}')