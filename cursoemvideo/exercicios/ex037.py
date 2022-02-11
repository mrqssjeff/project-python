n1 = 0
num = int(input('Digite um número inteiro: '))
ops = int(input('''[ 1 ] Binário.
[ 2 ] Octal.
[ 3 ] Hexadecimal.
Selecione uma das opções de conversão acima: '''))

lista = ('Binário','Octal','Hexadecimal')

if ops == 1:
    n1 = bin(num)
elif ops == 2:
    n1 = oct(num)
elif ops == 3:
    n1 = hex(num)

print(f'O valor {num} convertido para {lista[ops -1]} é {n1[2:]}')