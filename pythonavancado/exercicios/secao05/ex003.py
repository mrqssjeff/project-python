import math
num = float(input('Digite um número: '))
if num >= 1:    
    num1 = math.pow(num, 1/2)
    print(f'A raiz quadrda de {num} é {num1}')
else:
    num2 = num ** 2
    print(f'O número {num} elevado ao quadrado é {num2}')