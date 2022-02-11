from time import sleep
print('\033[32mContagem regressiva para o Réveillon...\033[m')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[32mFeliz Ano Novo!\033[m')