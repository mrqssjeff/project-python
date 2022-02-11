from datetime import date
per = int(input('Digite o ano que quer analizar. Se quiser analizar o ano atual digite 0:  '))
if per == 0:
    per = date.today().year
elif per % 4 == 0 and per % 100 != 0 or per % 400 == 0:
    print('O ano \033[1mé\033[m bissexto!')
else:
    print('O ano \033[1mnão é\033[m bissexto!')