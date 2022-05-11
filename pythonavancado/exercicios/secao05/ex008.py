while True:
    nota1 = float(input('Digite a 1º nota: '))
    if nota1 < 0.0 or nota1 > 10.0:
        nota1 = float(input('Nota Inválida! Digite novamente: '))
    nota2 = float(input('Digite a 2ª nota: '))
    if nota2 < 0.0 or nota2 > 10.0:
        nota2 = float(input('Nota Inválida! Digite novamente: '))
    media = (nota1 + nota2) / 2
    print(f'Sua média foi de {media}.')
    break
