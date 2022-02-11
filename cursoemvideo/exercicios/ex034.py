sal = float(input('Digite o valor do seu salário para calcular seu aumento: R$ '))
aumento = sal + (sal * 0.10)
aumento2 = sal + (sal * 0.15)
if sal >1250.00:
    print(f'\033[35mO valor do seu aumento será de 10%, e seu novo salário será de R${aumento:.2f}\033[m ')
else:
    print(f'\033[31mO valor do seu aumento será de 15%, e seu novo salário será de R${aumento2:.2f}\033[m ')