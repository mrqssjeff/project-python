produto = float(input('Informe o valor do produto: R$ '))
desconto = produto * 0.90
print(f'''\nO produto com 10% de desconto é R${desconto:.2f}
\nO valor em 3 parcelas sem juros é R${produto / 3:.2f}
\nA comissão do vendedor para a compra à vista é R${desconto * 0.05:.2f}
\nA comissão do vendedor para venda parcelada é de R${produto * 0.05:.2f}''')