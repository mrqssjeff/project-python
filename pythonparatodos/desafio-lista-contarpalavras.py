lista = list()
while True:
    palavra = str(input('Informe uma palavra [0 para sair]: ')).strip()
    if palavra == str(0):
        break  
    lista.append(palavra)       
info = input('Informe a palavra que deseja contar: ')                
print(f'A palavra {info} está contida {lista.count(info)} vezes na lista.')  
