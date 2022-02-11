numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado! Não vou adicionar')
    per = ' '
    while per not in 'SN':
        per = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if per == 'N':
        break
print(f'Você digitou os valores {numeros}')
