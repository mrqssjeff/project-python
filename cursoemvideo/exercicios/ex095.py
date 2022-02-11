jogador = dict()
time = list()
partidas = list()
while True:
    partidas.clear()
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    for c in range(0, tot):
        num = int(input((f'Quantos gols na partida {c}?: ')))
        partidas.append(num)
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if res in 'SN':
            break
        print('Erro. Responda apenas S ou N')
    if res == 'N':
        break
print('-'*40)
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Digite um número válido.')
    else:
        print(f'Levantamento do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('-'*40)
print('Volte sempre!')
