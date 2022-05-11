altura = float(input('Informe sua altura (em metros): '))
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso}')
elif sexo == 'F':
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso}')
else:
    print('Erro! Tente abrir o programa novamente.')