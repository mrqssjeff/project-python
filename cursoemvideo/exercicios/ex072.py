extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    while num > 20 or num < 0:
        num = int(input('Inválido. Digite novamente um número de 0 a 20: '))
    if num >=0 and num <= 20:
        print(f'O número {num} por extenso é {extenso[num]}')
    per = ' '
    while per not in 'SN':
        per = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]
    if per == 'N':
        print('Finalizando...')
        break
