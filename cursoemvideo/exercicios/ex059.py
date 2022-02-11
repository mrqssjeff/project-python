from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
res = 0
while res != 5:
    res = int(input('''Selecione a operação.
    [1] Somar 
    [2] Multiplicar 
    [3] Maior 
    [4] Novos números 
    [5] Sair do programa
     >>>>Qual sua opção?: '''))
    if res == 1:
        print(f'A soma entre {n1} e {n2} vale {n1 + n2} ')
    elif res == 2:
        print(f'A multiplicação entre {n1} e {n2} vale {n1 * n2} ')
    elif res == 3:
        if n1 > n2:
            print(f'O maior número é {n1} ')
        elif n2 > n1:
            print(f'O maior número é {n2} ')
        else:
            print('Os valores são iguais.')
    elif res == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro número: '))
    elif res == 5:
        print('Programa finalizado!')
    elif res <= 0 or res > 5:
        print('Opção inválida. Tente novamente. ')
    sleep(1)