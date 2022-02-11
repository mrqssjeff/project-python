dados = list()
total = list()
maispesada = maisleve = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')).strip().capitalize())
    dados.append(float(input('Digite o peso: ')))
    if len(total) == 0:
        maispesada = maisleve = dados[1]
    else:
        if dados[1] > maispesada:
            maispesada = dados[1]
        if dados[1] < maisleve:
            maisleve = dados[1]
    total.append(dados[:])
    dados.clear()
    per = ' '
    while per not in 'SN':
        per = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if per == 'N':
        break
print(f'Foram cadastradas {len(total)} pessoas ')
print(f'A pessoa mais pesada é ', end='')
for p in total:
    if p[1] == maispesada:
        print(f'{p[0]} com {maispesada} Kg', end='')
print(f'\nA pessoa mais leve é ', end='')
for p in total:
    if p[1] == maisleve:
        print(f'{p[0]} com {maisleve}Kg')

