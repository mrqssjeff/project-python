primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
adicao = float(input(f'Informe o resultado da operação: {primeiro} + {segundo} = '))
if primeiro + segundo == adicao:
    print('Parabéns, você acertou.')
else:
    print(f'Você errou! O resultado da operação é: {primeiro + segundo}')
subtracao = float(input(f'Informe o resultado da operação {primeiro} - {segundo} = '))
if primeiro - segundo == subtracao:
    print('Parabéns! Você acertou.')
else:
    print(f'Você errou! O resultado da operação é: {primeiro - segundo}')
multi = float(input(f'Informe o resultado da operação: {primeiro} x {segundo} = '))
if primeiro * segundo == multi:
    print('Parabéns! Você acertou.')
else:
    print(f'Você errou! O resultado da operação é: {primeiro * segundo} ')
divisao = float(input(f'Informe o resultado da operação: {primeiro} : {segundo} = '))
if primeiro / segundo == divisao:
    print('Parabéns! Você acertou.')
else:
    print(f'Você errou! O resultado da operação é: {primeiro / segundo} ')
