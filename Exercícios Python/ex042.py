r1 = float(input('Digite o comprimento do primeiro seguimento: '))
r2 = float(input('Digite o comprimento do segundo seguimento: '))
r3 = float(input('Digite o comprimento do terceiro seguimento: '))

if abs(r1 - r2) < r3 < r1+r2 and abs(r1 - r3) < r2 < r1+r3 and abs(r2 - r3) < r1 < r2+r3:
    print('É possível formar um triângulo com os comprimentos {}, {} e {} '.format(r1, r2, r3), end='')
    if r1 == r2 == r3:
        print('e ele é EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('e ele é ISÓSCELES.')
    else:
        print('e ele é ESCALENO.')
else:
    print('Não é possível formar um triângulo com estes comprimentos.')
