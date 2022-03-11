soma = 0
for c in range(0, 4):
    nota = float(input(f'Digite o valor da {c+1}ª nota: '))
    soma += nota
media = soma / 4
print(f'O valor da média aritmética entre as notas é {media:.2f}')
