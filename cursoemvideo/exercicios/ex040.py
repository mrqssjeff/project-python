print('\033[32mCalcule a media de suas notas! \033[m')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi de {media:.1f}! Que pena, você foi reprovado! ')
elif media>=5.0 and media<=6.9:
    print(f'Sua média foi de {media:.1f}! Quase lá, você ficou de recuperação!')
else:
    print(f'Sua média foi de {media:.1f}! Parabéns, você foi aprovado!')