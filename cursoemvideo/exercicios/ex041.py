print('\033[32mDescubra em que categoria você está na Confederação Nacional de Natação!\033[m')
idade = int(input('Digite sua idade: '))
if idade<=9:
    print('Você está na categoria \033[34mMirim\033[m!')
elif idade>9 and idade<=14:
    print('Você está na categoria \033[34mInfantil\033[m!')
elif idade>14 and idade<=19:
    print('Você está na categoria \033[34mJúnior\033[m!')
elif idade>19 and idade <=25:
    print('Você está na categoria \033[34mSênior\033[m!')
else:
    print('Você está na categoria \033[34mMaster\033[m!')
