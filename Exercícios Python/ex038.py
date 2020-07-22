int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite outro número inteiro: '))

# Comparação
if int1 > int2:
    print('O número {} é maior que {}'.format(int1, int2))
elif int2 > int1:
    print('O número {} é maior que {}'.format(int2, int1))
else:
    print('Os dois números são iguais.')
