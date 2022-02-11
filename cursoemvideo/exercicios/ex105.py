def notas(*n, sit=False):
    lista = dict()
    lista['Total'] = len(n)
    lista['Maior'] = max(n)
    lista['Menor'] = min(n)
    lista['Média'] = sum(n) / len(n)
    if sit:
        if lista['Média'] < 5:
            lista['Situação'] = 'Reprovado'
        if lista['Média'] >= 5 and lista['Média'] < 7:
            lista['Situação'] = 'Recuperação'
        if lista['Média'] >= 7:
            lista['Situação'] = 'Aprovado'
    return lista


resp = notas(9, 8.7, 4, 5, sit=True)
print(resp)
