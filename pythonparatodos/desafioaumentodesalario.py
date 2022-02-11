salario = float(input('Digite o valor do salário atual: R$'))
aumento = float(input('Digite o percentual de aumento: '))
print(f'O valor do salário com {aumento}% de aumento é R${salario + (salario * (aumento / 100)):.2f} ')