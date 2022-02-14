lista = list()
pares = list()
impar = list()
while True:
    num = int(input('Informe um número [0 para sair]: '))
    if num == 0:
        break
    lista.append(num)
for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impar.append(item)
print(f'Números pares: {pares}')
print(f'Números ímpares: {impar}')
