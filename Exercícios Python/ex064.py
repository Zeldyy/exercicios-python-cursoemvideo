n = soma = c = 0
while n != 999:
    n = int(input('Digite o valor: (999 para parar) '))
    if n != 999:
        soma += n
        c += 1
print('Foram digitados {} valores e a soma deles é {}.'.format(c, soma))
