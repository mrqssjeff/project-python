numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número digitado é \033[97;40mpar\033[m!')
else:
    print('O número digitado é \033[35;40mímpar\033[m!')
