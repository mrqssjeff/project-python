salario = float(input('Informe seu salário: '))
emprestimo = float(input('Informe o valor da prestação do empréstimo: '))
if emprestimo > (salario * 0.2):
    print('Emréstimo negado!')
else:
    print('Empréstimo concedido!')