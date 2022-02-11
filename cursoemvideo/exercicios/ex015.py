q = float(input('Qual a quantidade de kilômetros percorridos?'))
d = float(input('Qual a quantidade de dias pelos quais ele foi alugado?'))
print(f'O preço a ser pago totalizando a quantidade de km percorridos mais a quantidade de dias é de R${(q * 0.15) + (d * 60):.2f}')