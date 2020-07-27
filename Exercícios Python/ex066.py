'''n = soma = c = 0
while n != 999:
    n = int(input('Digite o valor: (999 para parar) '))
    if n != 999:
        soma += n
        c += 1
print('Foram digitados {} valores e a soma deles é {}.'.format(c, soma))
'''
c = soma = 0
while True:
    n = int(input('Digite um valor: (999 para parar)'))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Foram digitados {c} valores e a soma deles é {soma}.')