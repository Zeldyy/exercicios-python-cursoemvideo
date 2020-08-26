from time import sleep
def contador(inicio, fim, passo):
    erro = False
    if (fim - inicio) > 0:
        final = fim + 1
        if passo < 0:
            passo = abs(passo)
        elif passo == 0:
            passo = 1
    elif (fim - inicio) < 0:
        final = fim - 1
        if passo > 0:
            passo *= (-1)
        elif passo == 0:
            passo = -1
    else:
        print(f'Erro! O início e o fim devem ser valores diferentes.')
        erro = True
    titulo(f'Contador de {inicio} a {fim} de {abs(passo)} em {abs(passo)}')
    if erro is False:
        print('Contagem: ', end = '')
        for c in range(inicio, final, passo):
            print(c, end='  ')
            sleep(0.4)
        print()
def titulo(txt):
    comp = len(txt) + 4
    print('-' * comp)
    print(f'  {txt}  ')
    print('-' * comp)


contador(1, 10, 1)
contador(10, 0, -2)
print('-'* 30)
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)
