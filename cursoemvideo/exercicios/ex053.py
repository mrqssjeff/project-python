frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Você digitou a frase {frase}')
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo.')