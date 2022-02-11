from random import randint
from time import sleep
comp = randint(0, 10)
print('Olá. Sou seu computador!')
sleep(1)
print('Acabei de pensar em número de 0 a 10...')
sleep(1)
print('Advinhe qual é!')
sleep(1)
jog = int(input('Qual é seu palpite?: '))
palpite = 1
while jog != comp:
    palpite += 1
    if jog > comp:
        jog = int(input(('O número é menor... Tente mais uma vez: ')))
    else:
        jog = int(input('O número é maior... tente mais uma vez: '))
print(f'Parabéns, você acertou com {palpite} palpite(s)!')
