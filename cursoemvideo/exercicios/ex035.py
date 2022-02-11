print('---' * 20)
print('Descubra se três retas podem formar um triângulo!')
t1 = float(input('Digite a primeira reta: '))
t2 = float(input('Digite a segunda reta: '))
t3 = float(input('Digite a terceira reta: '))
if t1 + t2 > t3 and t1 + t3 > t2 and t3 + t2 > t1:
    print('\033[46mA formação do triângulo é possível!\033[m')
else:
    print('\033[44mA formação do triângulo não é possível!\033[m')
print('---' * 20)