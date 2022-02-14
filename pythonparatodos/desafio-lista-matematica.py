lista = list()
multi = 1
while True:
    num = int(input('Digite um número [0 para sair]: '))
    if num == 0:
        break
    lista.append(num)
    multi *= num
print(f'A soma entre os valores informados é: {sum(lista)}')
print(f'A multiplicação entre os valores informados é: {multi}')
print(f'O maior valor informado é: {max(lista)}')
print(f'O menor valor informado é: {min(lista)}')