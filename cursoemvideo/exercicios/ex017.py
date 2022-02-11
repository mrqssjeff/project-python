import math
co = float(input('Digite o cateto oposto do triângulo retângulo: '))
ca = float(input('Digite o cateto adjacente do triângulo retângulo: '))
print(f'A hipotenusa do triângulo retângulo é {math.hypot(co, ca):.2f}')