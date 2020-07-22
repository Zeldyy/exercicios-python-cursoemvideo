'''n = int(input('Digite um número inteiro: '))
print('Todos os pares que estão entre 1 e {} são: '.format(n))
for c in range (2, n+1, 2):
    print(c)'''

n = int(input('Digite um número inteiro: '))
print('Todos os pares que estão entre 1 e {} são: '.format(n))
for c in range (1, n+1):
    if c % 2 == 0:
        print(c)