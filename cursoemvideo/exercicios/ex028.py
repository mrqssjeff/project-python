from random import randint
from time import sleep
comp = randint(0, 5)
print('--- ' * 20)
print('Vou pensar em um número de 0 a 5. Advinhe qual é! \033[1mZEHAHAHAHAHA\033[m')
print('---' * 20)
jog = int(input('Digite um número de 0 a 5: '))
print('\033[34mProcessando...\033[m')
sleep(2)
if jog == comp:
    print('Você não acertou, tente novamente. O sonho de um homem nunca morre! \033[1mZEHAHAHAHAHAH\033[m')
else:
    print('Você acertou, parabéns! \033[1mZEHAHAHAHAH\033[m')