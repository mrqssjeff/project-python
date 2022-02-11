from random import sample


def maior(*num):
    for v in num:
        m = max(v)
        print(m)


c = 0
while c != 5:
    c += 1
    print('Analizando os valores passados...')
    a = sample(range(1, 20), 6-c)
    print(a)
    print(f'O maior valor formado foi ', end='')
    maior(a)
    print()
