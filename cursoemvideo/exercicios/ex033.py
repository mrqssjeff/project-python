n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
nums = [n1, n2, n3]
print(f'O \033[4mmaior\033[m número é {max(nums)}')
print(f'O \033[7;31mmenor\033[m número é {min(nums)}')
