hora = float(input('Informe o valor da hora de trabalho: R$ '))
valor = float(input('Informe quantas horas foram trabalhadas no mês: '))
total = hora * valor + (0.10 * (hora * valor))
print(f'O valor a ser pago para o funcionário é R${total:.2f}')
