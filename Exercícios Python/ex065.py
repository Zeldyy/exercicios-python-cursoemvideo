continuar = 'S'
media = 0
maior = 0
menor = 999
c = 0
soma = 0
while continuar == 'S':
    c += 1
    n = int(input('Digite um Valor: '))
    if c == 1: menor = n
    if n > maior: maior = n
    if n < menor: menor = n
    soma += n
    continuar = str(input('Gostaria de continuar? (S/N) ')).upper()
media = soma / c
print('A média dos valores digitados é {}; O menor valor é {} e o maior valor é {}.'.format(media, menor, maior))
