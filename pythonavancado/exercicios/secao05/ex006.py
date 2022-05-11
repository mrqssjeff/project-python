num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
while True:
    maior = menor = diferença = 0
    if num1 > num2:
        maior = num1
        menor = num2
    elif num2 > num1:
        maior = num2
        menor = num1
    else:
        maior = menor = num1
        diferença = 0
    diferença = maior - menor
    print(f'O maior número é {maior} e o menor número é {menor}.\nA diferença entre eles é {diferença}')
    break

