while True:
    soma = 0
    num = int(input('Digite um número inteiro(Maior que zero: '))
    x = [int(a) for a in str(num)]
    for i in x:
        soma += i
    if num != 0:
        print(f'A soma entre os números digitados é {soma}')
        break

