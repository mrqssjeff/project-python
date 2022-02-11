def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro. Digite um número inteiro válido. ')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro. Digite um número real válido. ')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


n1 = leiaInt(input('Digite um número inteiro: '))
n2 = leiafloat(input('Digite um número real: '))
print(f'Os números digitados foram {n1} e {n2}')
