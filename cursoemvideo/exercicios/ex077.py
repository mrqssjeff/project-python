nome = ('Rukia', 'Orihime', 'Nell',
            'Rangiku', 'Karin', 'Yachiru',
            'Kuukaku', 'Nemu', 'Yoruichi')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in nome:
    print(f'No nome {c} temos', end=' ')
    for d in vogais:
        if d in c:
            print(f'{d}', end=' ')
    print()
