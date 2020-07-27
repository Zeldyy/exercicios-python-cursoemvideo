'''n = int(input('Digite um número para saber seu fatorial: '))
c = n
fatorial = 1
while c != 0:
    fatorial = fatorial * c
    c -= 1
print('O fatorial de {} é {}.'.format(n, fatorial))
'''
n = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1
for c in range(n,0,-1):
    fatorial = c * fatorial
print('O fatorial de {} é {}.'.format(n, fatorial))
