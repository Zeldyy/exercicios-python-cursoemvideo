print('Programa que lê os 10 primeiros termos ou mais de uma Progressão aritmética.')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
termos_extras = 1
soma = 10
while termos_extras != 0:
    print('{}º Termo: {}'.format(c, p + (c-1)*r))
    c += 1
    if (c-1) == soma:
        termos_extras = int(input('Gostaria de saber mais quantos termos? '))
        soma += termos_extras
