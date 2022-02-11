jogador = dict()
gols = list()
soma = 0
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    for c in range(partidas):
        gols.append(int(input((f'Quantos gols na partida {c+1}?: '))))
    jogador['Gols'] = gols
    jogador['Total'] = sum(gols)
    print('-'*30)
    print(jogador)
    print('-'*30)
    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')
    print('-'*30)
    print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
    for pos, v in enumerate(gols):
        print(f'Na partida {pos+1}, fez {v} gols.')
    print(f'Foi um total de {jogador["Total"]} gols.')
    break