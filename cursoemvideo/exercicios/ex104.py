def leiaint(num=0):
    while True:
        num = input('Digite um número: ')
        if num.isnumeric():
            print(f'Você acabou de digitar o número {num}.') 
            break
        else:
            print('Erro! Digite um número inteiro válido!')       
       
        
leiaint()
