n = int(input('Digite um número para saber se ele é primo: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[33m', end=' ')
    print(f'{c}', end='')
print(f'\033[m \nO número {n} possui {total} divisores.')
if total == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')