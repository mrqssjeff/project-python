frase = input('Escreva seu nome completo: ').strip()
print(f'''Analizando seu nome...\n
O seu nome capitalizado é {frase.title()},\n'
O seu nome com todas as letras maiúsculas é {frase.upper()},\n
O número de letras do seu nome é {len(frase) - frase.count(' ')},\n
E seu primeiro nome tem {frase.find(" ")} letras\n
Seu primeiro nome é {frase.split()[0].capitalize()}\n
Seu último nome é {frase.split()[-1].capitalize()}''')