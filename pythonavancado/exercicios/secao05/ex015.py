num = int(input('Digite um número de 1 a 7: '))
if num == 1:
    print('Domindo é o 1º dia da semana!')
elif num == 2:
    print('Segunda-feira é o 2º dia da semana!')
elif num == 3:
    print('Terça-feira é o 3º dia da semana!')
elif num == 4:
    print('Quarta-feira é o 4º dia da semana!')
elif num == 5:
    print('Quinta-feira é o 5º dia da semana!')
elif num == 6:
    print('Sexta-feira é o 6º dia da semana!')
elif num == 7:
    print('Sábado é o 7º dia da semana!')
elif num < 1 or num > 7:
    print('ERRO! Número Inválido!')