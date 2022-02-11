from datetime import date
print('\033[32m---\033[m' * 20)
print('\033[32mDescubra se você está em regularidade com o alistamento militar obrigatório!\033[m')
per = int(input('Digite quantos anos você tem: '))
date.today().year
if per < 18:
    print(f'Ainda falta(m) {18 - per} ano(s) para você se alistar! ')
elif per == 18:
    print(f'Você está na idade de alistamento!')
else:
    print(f'Já se passaram {per - 18} ano(s) da idade de alistamento! Faça o quanto antes!')
print('\033[32m---\033[m' * 20)

