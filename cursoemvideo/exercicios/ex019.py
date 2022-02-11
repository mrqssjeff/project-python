import random
n1 = input('Digite o nome do 1º aluno: ')
n2 = input('Digite o nome do 2º: ')
n3 = input('Digite o nome do 3º: ')
n4 = input('Digite o nome do 4º: ')
lista = n1, n2, n3, n4
print(f'O nome do aluno sorteado é {random.choice(lista)}')
