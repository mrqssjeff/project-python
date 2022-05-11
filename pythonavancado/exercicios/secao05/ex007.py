num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
maior = menor = diferença = 0
if num1 > num2:
    maior = num1
    menor = num2
elif num2 > num1:
    maior = num2
    menor = num1
else:
    diferença = 0
diferença = maior - menor
if diferença != 0:
    print(f'O maior número entre {num1} e {num2} é {maior}.')
else:
    print('Números iguais.')