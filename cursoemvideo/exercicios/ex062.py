print('Gerador de PA!')
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
prox = pt
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(prox, '→', end=' ')
        prox = pt + razao
        pt = prox
        c += 1
    print('Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print(f'Progressão finalizada com {total} termos.')

