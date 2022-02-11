print('\033[32mCalcule seu IMC!\033[m ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc<18.5:
    print(f'Seu IMC é de {imc:.1f}! Isso significa que você está abaixo do peso!')
elif imc>=18.5 and imc<25:
    print(f'Seu IMC é de {imc:.1f}! Isso significa que você está no peso ideal!')
elif imc>=25 and imc<30:
    print(f'Seu IMC é de {imc:.1f}! Isso significa que você está com Sobrepeso!')
elif imc>=30 and imc<40:
    print(f'Seu IMC é de {imc:.1f}! Isso significa que você está com Obesidade!')
else:
    print(f'Seu IMC é de {imc:.1f}! Isso significa que você está com Obesidade Mórbida!')
