print('Cadastre uma pessoa! ')
maiordeidade = homens = mulheres = 0
while True:
    print('-'*15)
    idade = int(input('Idade: '))
    if idade > 18:
        maiordeidade += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*15)
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-'*15)
print(f'''Total de pessoas com mais de 20 anos: {maiordeidade}
Ao todo temos {homens} homens cadastrados.
E temos {mulheres} mulheres com menos de 20 anos''')

