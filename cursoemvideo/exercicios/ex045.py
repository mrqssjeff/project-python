from random import randint
from time import sleep
comp = randint(0, 2)
lista = ('Pedra', 'Papel', 'Tesoura')
print('\033[32mBem vindo ao Mundo dos Games! O jogo de hoje será Jokenpô!\033[m')
print('Escolha sua jogada!')
jogador = int(input('''[0] Pedra.
[1] Papel.
[2] Tesoura.
Escolha sua opção: '''))
if jogador < 0 or jogador > 2:
    print('Opção Invalida. Tente novamente!')
    exit()
sleep(1)
print('\033[32mJo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!\033[m')
sleep(1)
print(f'O computador escolheu {lista[comp]}')
print(f'Jogador escolheu {lista[jogador]}!')
if comp == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Você ganhou')
    elif jogador == 2:
        print('Você perdeu')
if comp == 1:
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('Deu empate!')
    elif jogador == 2:
        print('Você ganhou!')
if comp == 2:
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Deu empate!')
