def metade(p=0, formato=False):
    res = p / 2
    return res if not formato else moeda(res)


def dobro(p=0, formato=False):
    res = p * 2
    return res if not formato else moeda(res)


def aumentar(p=0, t=0, formato=False):
    res = p + (p * (t / 100))
    return res if formato is False else moeda(res)


def diminuir(p=0, t=0, formato=False):
    res = p - (p * (t / 100))
    return res if formato is False else moeda(res)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')



def resumo(p, t=0, n=0):    
    print('-'*20)
    print('Resumo do valor'.center(20))
    print('-'*20)
    print(f'Preço analizado: {p:.2f}'.replace('.', ','))
    print(f'Dobro do preço: {dobro(p, True)}')
    print(f'Metade do preço: {metade(p, True)}')
    print(f'{t}% de aumento: {aumentar(p, t, True)}')
    print(f'{n}% de redução: {diminuir(p, n, True)}')

