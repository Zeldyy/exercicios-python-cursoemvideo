print('Programa que lê os 10 primeiros termos de uma Progressão aritmética.')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
while c != 11:
    print('{}º Termo: {}'.format(c, p + (c-1)*r))
    c += 1
