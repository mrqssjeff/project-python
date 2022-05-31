print('Calcule sua média ponderada e descubra se passou no exame!')
nota1 = float(input('Digite 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
media = (nota1 + nota2 + (nota3 * 2)) / 4
if media < 60:
    print(f'Sua média foi de {media}. Você foi REPROVADO!')
else:
    print(f'Sua média foi de {media}. Você foi APROVADO!')