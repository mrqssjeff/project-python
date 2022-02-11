print('---' * 20)
print('\033[34mDescubra se o empréstimo bancário para a compra de seu imóvel será aprovado.\33[m')
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite seu salário: R$ '))
anos = int(input('Digite a quantidade de anos em que deseja pagar: '))
pagamento = casa / (anos * 12)
minimo = salario * 0.30
if pagamento > minimo:
    print('O empréstimo será negado.')
else:
    print(f'O empréstimo pode ser concedido! O valor da prestação mensal do seu empréstimo será de R${pagamento:.2f}')
print('---' * 20)

