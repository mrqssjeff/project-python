somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print(f'---{p}ª Pessoa---')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho tem {maiorhomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
