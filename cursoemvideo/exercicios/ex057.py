sexo = str(input('Digite seu sexo: [M/F] ')).strip().lower()[0]
while sexo not in 'MmFf':
    sexo = str(input('Inválido. Tente novamente: ')).strip().lower()[0]
print('Sexo registrado com sucesso!')
