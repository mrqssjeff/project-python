import moeda

preço = float(input('Digite o preço: '))
print(f'''A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}
O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}
Aumentado 15%, temos {moeda.aumentar(preço, 15, True)}
Reduzindo 23%, temos {moeda.diminuir(preço, 23, True)}''')