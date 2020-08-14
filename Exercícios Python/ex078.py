lista = list()
menor = maior = 0
for c in range(0,5):
    lista.append(int(input(f'Digite o valor na posição {c}: ')))
    if c == 0:
        menor = maior = lista[c]
    if lista[c] <= menor:
        menor = lista[c]
    if lista[c] >= maior:
        maior = lista[c]
print(lista)
print(f'Maior valor: {maior} na posição ', end = '')
for c, num in enumerate(lista):
    if maior == num:
        print(f'{c} ', end = '')
print(f'\nMenor valor: {menor} na posição ', end = '')
for c, num in enumerate(lista):
    if menor == num:
        print(f'{c} ', end = '')
