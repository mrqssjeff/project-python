from random import sample
st = sample(range(1, 20), 5)


def sorte(*num):
    print(f'Sorteando 5 valores da lista: {st}')


sorte()


def pares(*num):
    soma = 0
    for v in st:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos valores pares de {st} é {soma}')


pares()
