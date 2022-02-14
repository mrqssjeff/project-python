lista = list()
listasemrep = list()
listarep = list()
while True:
    num = int(input('Informe um número [0 para sair]: '))
    if num == 0:
        break
    lista.append(num)
for item in lista:
    if item not in listasemrep:
        listasemrep.append(item)
    else:
        if item not in listarep:
            listarep.append(item)
print(f'Números informados: {lista}')
print(f'Números repetidos: {listarep}')
print(f'Números sem repetição: {listasemrep}')
