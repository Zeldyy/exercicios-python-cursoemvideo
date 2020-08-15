pessoas = list()
dado = list()
maior_peso = menor_peso = 0
while True:
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    continuar = str(input('Deseja continuar cadastrando? (S/N) ')).lower().strip()[0]
    if continuar in 'Nn':
        break
# Verificação de Peso
for c in range(0, len(pessoas)):
    if c == 0:
        maior_peso = menor_peso = pessoas[c][1]
    else:
        if pessoas[c][1] > maior_peso:
            maior_peso = pessoas[c][1]
        elif pessoas[c][1] < menor_peso:
            menor_peso = pessoas[c][1]
# Output
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Maior peso: {maior_peso}, da(s) pessoa(s) ', end='')
for p in pessoas:
    if maior_peso == p[1]:
        print(f'{p[0]} ', end='')
print(f'\nMenor peso: {menor_peso}, da(s) pessoa(s) ', end='')
for p in pessoas:
    if menor_peso == p[1]:
        print(f'{p[0]} ', end='')
