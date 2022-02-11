n = 0
while True:
    tab = int(input("Deseja ver a tabuada de qual valor?: "))
    if tab <= -1:
        break
    for n in range(0, 11):
        print(f'{n} x {tab} = {n * tab}')
print('Tabuada encerrada. Volte sempre!')
