cadastro = list()
while True:
  pessoa = {'nome': str(input('Nome: ')).strip(),
            'sexo': str(input('Sexo (M/F): ').strip().lower()[0]),
            'idade': int(input('Idade: '))}
  cadastro.append(pessoa)
  cont = str(input('Deseja continuar (S/N): ')).strip().lower()[0]
  if cont in 'Nn':
    break
print(cadastro)
print(f'Ao total, foram cadastradas {len(cadastro)} pessoas.')
# média da idade
soma_idade = 0
for pessoa in cadastro:
  soma_idade += pessoa['idade']
media_idade = soma_idade/len(cadastro)
print(f'A média de idade é {media_idade:.0f} anos.')
# Lista das mulheres
print('Pessoas do sexo Feminino:')
for pessoa in cadastro:
  if pessoa['sexo'] == 'f':
    print(f'=> {pessoa["nome"]}, com {pessoa["idade"]} anos.')
# Lista com pessoas acima da média
print('Lista com pessoas acima da média:')
for pessoa in cadastro:
  if pessoa['idade'] > media_idade:
    print(f'=> {pessoa["nome"]}, com {pessoa["idade"]} anos e do sexo', end=' ')
    print(f'Masculino' if pessoa['sexo'] == 'm' else f'Feminino')
