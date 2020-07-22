n = int(input('Digite um número inteiro: '))
t = int(input('Digite o tamanho da tabuada: '))
for c in range(0, t+1):
    print('{} x {} = {}'.format(c, n, c*n))