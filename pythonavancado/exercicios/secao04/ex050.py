from datetime import date
atual = date.today().year
anos = int(input('Informe quantos anos você tem: '))
birth = atual - anos
print(f'Você nasceu no ano de {birth}')
