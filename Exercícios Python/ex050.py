numeros = [0, 0, 0, 0, 0, 0]
print('Digite 6 números inteiros, que direi a soma dos pares: ')
s = 0
for c in range(0, 6):
    numeros[c] = int(input('{}º número: '.format(c+1)))
    if numeros[c] % 2 == 0:
        s += numeros[c]
print('Os números digitados foram {}, e a soma dos pares é {}'.format(numeros, s))