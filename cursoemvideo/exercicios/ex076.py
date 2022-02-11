devilfruits = ('Gomu Gomu No Mi', 5000000000, 'Ope Ope No Mi', 4500000000,
            'Hito Hito No Mi: Model Human', 50, 'Mera Mera No Mi', 1000000000,
            'Yami Yami no Mi', 3200000000, 'Yuki Yuki no Mi', 2200000000,
            'Gura Gura no Mi', 4300000000, 'Caesar Clown Smile', 100,
            'Tori Tori No Mi: Model Phoenix', 3800000000)
print(f'-'*15, 'AKUMAS NO MI', '-'*15)
for c in devilfruits:
    if type(c) is str:
        print(f'{c:.<38}', end=' ')
    else:
        print(f'{c} B$')
