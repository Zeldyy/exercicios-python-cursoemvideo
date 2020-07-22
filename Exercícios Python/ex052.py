n = int(input('Digite um número inteiro: '))
primo = 's'
if n == 2:
    print('O número 2 é primo.')
elif n == 1:
    print('O número 1 não é primo.')
else:
    for c in range(2, n):
        if n % c == 0:
            primo = 'n'
    if primo == 's':
        print('O número {} é primo.'.format(n))
    else:
        print('O número {} não é primo.'.format(n))
