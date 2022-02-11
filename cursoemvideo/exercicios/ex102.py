def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número:
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não os cálculos.
    :return: O valor do fatorial.
    """
    f = 1    
    c = num 
    if show==True:        
        while c > 0:
            print(c, end='')
            print(' x ' if c > 1 else ' = ' f'{f}', end='')
            f *= c
            c -= 1
        return f  
    if show==False:
        while c > 0:            
            f *= c
            c -= 1 
        return f 
              
          
n = int(input('Deseja calcular o fatorial de qual valor?: '))   
e = ' '
while e not in 'SN':
    e = str(input('Deseja mostrar o calculo completo? [S/N]: ')).strip().upper()[0]   
    if e == 'S':
        print(f'\nO fatorial de {n} é igual a {fatorial(n, True)}.')
    if e == 'N':
        print(f'O fatorial de {n} é igual a {fatorial(n)}.')
