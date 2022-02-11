per = int(input('Qual a distância da viagem em KM? '))
if per <=200:
    print(f'Numa viagem de {per}km o \033[7;45mpreço da passagem\033[m será R${per * 0.50:.2f}')
else:
    print(f'Numa viagem de {per}Km o \033[7;36mpreço da passagem\033[m será R${per * 0.45:.2f}')