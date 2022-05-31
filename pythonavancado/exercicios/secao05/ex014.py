nota1 = float(input('Informe sua nota do Trabalho de Laboratório: '))
nota2 = float(input('Informe sua nota da Avaliação semestral: '))
nota3 = float(input('Informe sua nota do Exame Final:  '))
media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
if media <= 2.9:
    print(f'Sua média foi de {media:2f}. Você foi REPROVADO!')
elif 3 <= media <= 4.9:
    print(f'Sua média foi de {media:2f}. Você está de RECUPERAÇÃO!')
else:
    print(f'Sua média foi de {media:2f}. Você foi APROVADO!')
