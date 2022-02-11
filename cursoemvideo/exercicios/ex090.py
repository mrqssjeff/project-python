aluno = {}
aluno['nome'] = str(input('Digite o nome: '))
aluno['média'] = float(input('Digite a média: '))
print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["média"]}')
if aluno['média'] >= 6:
    aluno['situacao'] = 'Aprovado'
elif aluno['média'] < 7 and aluno['média'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f'A situação do aluno é {aluno["situacao"]}')
