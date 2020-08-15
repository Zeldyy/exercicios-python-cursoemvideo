aluno = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} do aluno é {v}')
