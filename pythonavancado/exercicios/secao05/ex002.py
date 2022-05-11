import math
num = int(input('Digite um número para calcular sua raiz quadrada: '))
if num > 0:
    num1 = math.isqrt(num)
    print(f'A raiz quadrada de {num} é {num1}')
else:
    print('ERRO! Digite um número válido.')
