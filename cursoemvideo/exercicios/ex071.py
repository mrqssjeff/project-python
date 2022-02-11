print('Bem vindo ao Banco JFM!')
while True:
    valor = int(input((f'Digite o valor que quer sacar: R$')))
    cinquenta = valor // 50
    restoum = valor - (cinquenta * 50)
    if cinquenta >= 1:
        print(f'Total de {cinquenta} cédulas de R$50,00')
    vinte = restoum // 20
    restodois = restoum - (vinte * 20)
    if vinte >= 1:
        print(f'Total de {vinte} cédulas de R$20,00')
    dez = restodois // 10
    restotres = restodois - (dez * 10)
    if dez >= 1:
        print(f'Total de {dez} cédulas de R$10,00')
    if restotres >= 1:
        print(f'Total de {restotres} cédulas de R$1,00')
    break
print('Operação encerrada! Volte sempre!')