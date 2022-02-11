ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja sair? [S/N]: ')).strip().upper()
    if res == 'S':
        break
print(f'{"Nº:":<4} {"Nome:":<10} {"Média:":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    opcao = int(input('Mostrar notas de qual aluno? [999] para parar: '))
    if opcao == 999:
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('Volte sempre.')