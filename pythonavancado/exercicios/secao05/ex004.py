import math
num = float(input('Digite um número: '))
raiz = math.pow(num, 1/2)
quadrado = num ** 2
if num > 0:
    print(f'O número {num} elevado ao quadrado é {quadrado}. \nA raiz quadrada do número {num} é {raiz}.')
else:
    print('ERRO! Número inválido.')

