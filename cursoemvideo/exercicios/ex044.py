print('\033[35mCalcule o valor a ser pago pelo produto dada as condições de pagamento!\033[m ')
preço = float(input('Digite o preço do produto: '))
pagamento = int(input('''Escolha a opção de pagamento a seguir...\n'
[ 1 ] para à vista no dinheiro/cheque com 10% de desconto\n
[ 2 ] para à vista no cartão com 5% de desconto\n
[ 3 ] para Duas vezes no cartão com preço normal\n
[ 4 ] para Três vezes ou mais no cartão com 20% de juros: '''))
p1 = 1
p2 = 2
p3 = 3
if pagamento == p1:
    print(f'O preço do produto será de R${preço - (preço * 0.10):.2f}')
elif pagamento == p2:
    print(f'O preço do produto será de R$ {preço - (preço * 0.05):.2f}')
elif pagamento == p3:
    print(f'O preço do produto será de 2 parcelas de R$ {preço / 2:.2f}')
elif pagamento == 4:
    total = int(input('Em quantas parcelas deseja pagar?: '))
    parcela = (preço / total) + (preço * 0.20)
    print(f'O preço do produto será de {total} parcelas de R${parcela:.2f}')
else:
    print('Opção Inválida de pagamento. Tente novamente!')
