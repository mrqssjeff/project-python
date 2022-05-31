while True:
    num1 = num2 = 0
    menu = int(input('''
Selecione a operação matemática:
[1] para Adição
[2] para Subtração
[3] para Multiplicação 
[4] para Divisão
Informe sua escolha: '''))
    while menu < 1 or menu > 4:
        menu = int(input('Número inválido! Tente novamente: '))
    if 1 <= menu <= 4:
        num1 = float(input('Informe o primeiro número: '))
        num2 = float(input('Informe o segundo número: '))
    if menu == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}')
    elif menu == 2:
        menos = num1 - num2
        print(f'A subtração entre {num1} e {num2} é de {menos}')
    elif menu == 3:
        mult = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é {mult}')
    elif menu == 4:
        div = num1 / num2
        print(f'A divisão entre {num1} e {num2} é de {div}')
    res = int(input(
'''Deseja selecionar novos números e operação? 
[1] para Continuar
[Qualquer outro número] para SAIR: '''))
    if res == 0 or res > 1:
        print('Tenha um ótimo dia!')
        break
    elif res == 1:
        print('Menu: ')





