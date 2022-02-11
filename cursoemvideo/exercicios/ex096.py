def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l}x{c} é: {a}m²')


print('Controle de terrenos')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)

