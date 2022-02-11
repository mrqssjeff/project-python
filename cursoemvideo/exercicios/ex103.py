def jogador(txt, gol=0): 
    if not gol.isdigit():
        gol = 0  
    if txt == '':
        txt = '<desconhecido>'    
    return f'O jogador {txt} fez {gol} gols no campeonato!'

print(jogador(str(input('Nome do jogador: ')),
input('Número de gols: ')))
