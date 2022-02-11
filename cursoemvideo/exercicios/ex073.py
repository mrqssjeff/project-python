times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'RB Bragantino', 'Fluminense', 'América MG',
         'Atletico GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo',
         'Athletico Pr', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport Recife', 'Chapecoense')
print('-'*15)
print(f'Lista de times do Brasileirão: {times}')
print('-'*15)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-'*15)
print(f'Os 4 últimos são: {times[16:]}')
print('-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*15)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição.')