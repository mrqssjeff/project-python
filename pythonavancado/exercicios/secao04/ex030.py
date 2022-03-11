real = float(input('Digite o valor em Reais: R$ '))
cotacao = float(input('Digite o valor da cotação do Dólar: U$ '))
dolar = real / cotacao
print(f'R${real:.2f} corresponde a U${dolar:.2f}')
