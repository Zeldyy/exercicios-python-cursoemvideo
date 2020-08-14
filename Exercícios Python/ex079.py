lista = list()
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor repetido, portanto não foi adicionado.')
    continuar = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
lista_ord = lista[:]
lista_ord.sort()
print(f'Valores da lista: {lista_ord}')
