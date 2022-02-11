lista = list()
media = soma = 0
dados = dict()
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).strip().capitalize()
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if dados['Sexo'] not in 'FM':
        dados['Sexo'] = str(input('Erro! Por favor, digite apenas M ou F: ')).strip().upper()[0]
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    lista.append(dados.copy())
    res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if res not in 'SN':
        res = str(input('Erro! Responda apenas S ou N: ')).strip().upper()[0]
    if res == 'N':
        break
media = soma / len(lista)
print(f'Ao todo temos {len(lista)} pessoas cadastradas')
print(f'A média de idade é {media:.2f}')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end='')
print(f'\nLista de pessoas acima da média: ', end='')
for p in lista:
    if p['Idade'] >= media:
        print(f'{p["Nome"]}')
