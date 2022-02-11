valor = []
maior = menor = 0
for c in range(0, 5):
    valor.append(int(input(f'Digite o {c}º valor: ')))
    if c == 0:
        menor = maior = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c]
print(f'Os valores digitados foram {valor}')
print(f'O maior valor é {maior}', end= ' ')
for i, v in enumerate(valor):
    if v == maior:
        print(f'E está na posição {i}')
print(f'\nO menor valor é {menor}', end= ' ')
for i, v in enumerate(valor):
    if v == menor:
        print(f'E está na posição {i}')







