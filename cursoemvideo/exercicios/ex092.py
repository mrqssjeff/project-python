from datetime import date
cadastro = dict()
while True:
    cadastro['Nome'] = str(input('Nome: ')).strip()
    nas = int(input('Ano de Nascimento: '))
    idade = date.today().year - nas
    cadastro['Idade'] = idade
    cadastro['CTPS'] = int(input('Carteira de trabalho [0 não tem]: '))
    if cadastro['CTPS'] == 0:
        break
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = 60 - idade
    break
print('-'*30)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')


