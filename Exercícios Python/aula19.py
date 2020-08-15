estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for chave, valor in estado.items():
        print(f'O {chave} tem valor {valor}.')
