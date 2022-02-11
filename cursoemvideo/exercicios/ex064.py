n = int(input('Digite um número: [999] para parar: '))
cont = soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número: [999] para parar: '))
if n == 999:
    print(f'Você digitou {cont} números e a soma entre eles é {soma}')
