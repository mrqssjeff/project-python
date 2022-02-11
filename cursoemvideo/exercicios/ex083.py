lista = list()
exp = str(input('Digite uma expressão: '))
for simb in exp:
    if simb == '(':
        lista.append(simb)
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(simb)
            break
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não está válida!')