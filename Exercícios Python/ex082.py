continuar = 'S'
valores = []
pares = []
impares = []
while continuar == 'S':
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista com todos os valores é: {valores}')
print(f'A lista com valores pares é: {pares}')
print(f'A lista com valores ímpares é: {impares}')
