def metade(p=0):
    return p / 2


def dobro(p=0):
    return p * 2


def aumentar(p=0, t=1.15):
    au = p * t
    return au


def diminuir(p=0, t=0.77):
    di = p * t
    return di


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')


