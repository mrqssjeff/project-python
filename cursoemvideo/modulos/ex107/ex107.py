import moeda

preço = float(input('Digite o preço: '))
print(f'''A metade de {preço} é {moeda.metade(preço)},
O dobro de {preço} é {moeda.dobro(preço)}, 
Aumentado 15%, temos {moeda.aumentar(preço)}
Reduzindo 23%, temos {moeda.diminuir(preço)}''')