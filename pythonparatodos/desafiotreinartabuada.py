c = acertos = erros = 0
num = int(input('Digite um número que desejas treinar a tabuada: '))
while c < 11:
    res = int(input(f'Digite o resultado de {c} x {num} = '))
    if res == c * num:
        print('Resposta correta!')
        acertos += 1
    else:
        print(f'Resposta Incorreta! O valor correto é {c * num}. ')
        erros += 1
    c += 1
print(f'Total de acertos: {acertos}')
print(f'Total de erros: {erros}')
