print('Soma entre todos os números ímpares que são \nmúltiplos de 3 entre 1 e 500: ')
s = 0
for c in range(1, 501):
    print('\n{} '.format(c), end='')
    if c % 2 == 1:
        print(' é ímpar', end='')
        if c % 3 == 0:
            s += c
            print(' e é múltiplo de 3, será adicionado na soma. Parcial: {}'.format(s), end='')
print('\nSoma total: ', s)