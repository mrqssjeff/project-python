from time import sleep
num = int(input('Digite um número inteiro de 4 digitos: '))
numero = str(num)
print('Os digitos do número informado são: ')
for c in range(0, 4):    
    sleep(1)
    print(numero[c])
