import math
num = int(input('Digite um número inteiro: '))
if num >= 0:
    log = math.log(num)
    print(f'O logaritmo de {num} é {log}')
else:
    print('Número Inválido!')