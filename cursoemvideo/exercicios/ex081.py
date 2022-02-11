numeros = list()
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    per = ' '
    while per not in 'SN':
        per = str(input('Deseja sair? [S/N]: ')).strip().upper()[0]
    if per == 'S':
        break
print(f'Você digitou {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
