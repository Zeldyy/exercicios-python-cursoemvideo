from datetime import datetime
pessoa = {'nome': str(input('Nome: ')).strip(),
          'anonasc': int(input('Ano de Nascimento: ')),
          'idade': datetime.today().year - pessoa['anonasc'],
          'ctps': int(input('CTPS (0 se não tem): '))}
if pessoa['ctps'] != 0:
  pessoa['anocontrato'] = int(input('Ano de contratação: '))
  pessoa['salario'] = float(input('Salário: '))
  pessoa['idade_aposentado'] = pessoa['idade'] + 35 - (datetime.today().year - pessoa['anocontrato'])
for chave, valor in pessoa.items():
  print(f'{chave} tem o valor {valor}.')
