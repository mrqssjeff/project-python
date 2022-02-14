res = ' '
while res != "SIM":
    res = str(input('Você gosta de python?: ')).strip().upper()
    if res == 'SIM':
        print('Resposta correta. Finalizando o programa.')
        break
