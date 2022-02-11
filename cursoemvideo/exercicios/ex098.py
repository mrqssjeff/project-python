def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end=' ')
    print()




contagem(1, 10, 0)
contagem(10, 0, 2)
contagem(int(input('Digite o ínicio: ')),
         int(input('Ditite o fim: ')),
         int(input('Digite o passo: ')))