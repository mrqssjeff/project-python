frase = str(input('Digite alguma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} \033[0;32mvez/vezes\033[m')
print(f'A letra A aparece \033[1mprimeiro\033[m na posição {frase.find("A")+1}')
print(f'A letra A aparece a \033[7;37múltima\033[m vez na posição {frase.rfind("A")+1}')


