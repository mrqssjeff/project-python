print('\033[36mDescubra se três segmentos de reta podem formar um triângulo e de qual tipo ele é!\033[m')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and r1 == r2 == r3:
    print('A formação do triângulo é possível e ele é do tipo \033[31mEquilátero\033[m!')
elif r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and r1 == r2 or r1 == r3 or r3 == r2:
    print('A formação do triângulo é possível e ele será do tipo \033[31mIsósceles\033[m!')
elif r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 and r1 != r2 and r1 != r3 and r2 != r3:
    print('A formação do triângulo é possível e ele será do tipo \033[31mEscaleno\033[m!')
else:
    print('A formação do triângulo não é possível!')


