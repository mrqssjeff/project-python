print('Calcule os 10 primeiros termos de um PA!')
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
prox = pt
c = 1
while c <= 10:
    print(prox, "→", end=' ')
    prox = pt + razao
    pt = prox
    c += 1
print('Acabou!')
