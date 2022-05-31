print('Calcule a área de um trapézio!')
altura = float(input('Digite a altura: '))
basemenor = float(input('Digite a base menor: '))
basemaior = float(input('Digite a base maior: '))
area = ((basemaior + basemenor) * altura) / 2
if basemaior > 0 and basemenor > 0:
    print(f'A área do trapézio informado é {area}')
else:
    print('Algum valor foi informado incorretamente! Tente executar o prgrama outra vez.')
