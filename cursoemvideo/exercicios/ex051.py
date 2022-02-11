print('\033[34mDescubra os dez primeiros termos de uma Progressão Aritmética!\033[m')
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * razao
if razao == 0:
    print('A PA é constante.')
for c in range(pt, decimo + razao, razao):
 #   print(f'{c * r + pt}', end=" ")
    print(f'{c}', end=' ')
print('Acabou!')