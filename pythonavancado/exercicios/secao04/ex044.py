escada = float(input('Informe a altura do degrau da escada [em cm]: '))
total = float(input('Informe a altura que deseja alcançar: [em m] '))
alt = escada / 100
degrau = total // alt
print(f'Para alcançar a altura de {total} metros precisa-se subir {degrau:.0f} degraus.')