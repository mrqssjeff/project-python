import moeda

preço = float(input('Digite o preço: '))
print(f'''A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}
O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}
Aumentado 15%, temos {moeda.moeda(moeda.aumentar(preço))}
Reduzindo 23%, temos {moeda.moeda(moeda.diminuir(preço))}''')