vel = float(input('Em qual velocidade você está dirigindo? '))
multa = (vel - 80) * 7
if vel >=80:
    print(f'O limite de velocidade foi excedido! Que pena, você foi \033[1;33mmultado\033[m! A multa será no valor de R${multa:.2f}!')
else:
    print('Continue dirigindo com \033[36msegurança\033[m! Tenha um bom dia!')
