from random import shuffle
n1 = input('Nome do 1º aluno: ')
n2 = input('Nome do 2º: ')
n3 = input('Nome do 3º: ')
n4 = input('Nome do 4º: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A lista será na ordem: {lista}')

