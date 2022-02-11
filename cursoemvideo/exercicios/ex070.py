print('Lojas Mugiwara Kaizokudan!')
print('-'*15)
soma = maisdemil = contador = barato = 0
maisbarato = ' '
while True:
    produto = str(input('Nome do produto?: '))
    valor = float(input('Valor do produto B$ '))
    contador += 1
    soma += valor
    if valor > 1000.00:
        maisdemil += 1
    if contador == 1:
        barato = valor
        maisbarato = produto
    else:
        if valor < barato:
            barato = valor
            maisbarato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if cont == 'N':
        break
print('-'*10, 'Fim do programa!', '-'*10)
print(f'''O total da compra foi de ${soma:.2f} Berries
Temos {maisdemil} produtos que custam mais de $1000,00 Berries
O produto mais barato foi {maisbarato} que custa ${barato:.2f} Berries''')

