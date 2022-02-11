res = 'S'
cont = soma = maior = menor = 0
while res in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print('Acabou')

