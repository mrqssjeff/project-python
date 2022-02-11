from random import randint
print('Vamos jogar par ou ímpar!')
print('-'*15)
comp = randint(0, 10)
while True:
   valor = int(input('Digite um valor: '))
   soma = comp + valor
   parouimpar = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
   while parouimpar not in 'PI':
      parouimpar = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0]
   if soma % 2 == 0 and parouimpar in 'P':
      print(f'Você jogou {valor}, o computador jogou {comp}. A soma deu {soma}. Número par. Parabéns você ganhou!')
      print('Vamos jogar novamente...')
   elif soma % 2 != 0 and parouimpar in 'I':
      print(f'Você jogou {valor}, o computador jogou {comp}. A soma deu {soma}. Número Ímpar. Parabéns Você ganhou')
      print('Vamos jogar novamente...')
   elif soma % 2 == 0 and parouimpar in 'I':
      print(f'Você jogou {valor}, o computador jogou {comp}. A soma deu {soma}. Número par. Você perdeu! GAME OVER.')
      break
   elif soma % 2 != 0 and parouimpar in 'P':
      print(f'Você jogou {valor}, o computador jogou {comp}. A soma deu {soma}. Número Ímpar. Você perdeu! GAME OVER!')
      break


