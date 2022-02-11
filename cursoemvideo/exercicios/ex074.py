#método errado
# from random import randint
# menor = maior = 0
# print('Os valores sorteados foram:', end=' ')
# for c in range(0, 5):
#     int = randint(0, 100)
#     if c == 1:
#         menor = maior = int
#     else:
#         if int > maior:
#             maior = int
#         if int < menor:
#             menor = int
#     print(int, end=' ')
# print('\nO menor valor foi ', menor)
# print('O maior valor foi ', maior)

from random import randint
num = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
print(f'Os valores sorteados foram: ', end=' ')
for n in num:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

