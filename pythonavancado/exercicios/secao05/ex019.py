num = int(input('Digite um número inteiro: '))
if num / 3 == 0 and num / 5 == 0:
    print(f'O número {num} é dívisível por 3 e 5.')
elif num / 3 == 0 and num / 5 != 0:
    print(f'O número {num} é divisível por 3 mas não por 5.')
elif num / 3 != 0 and num / 5 == 0:
    print(f'O número {num} não é divisível por 3 mas é divisível por 5.')
elif num is float:
    print('Número inválido.')
