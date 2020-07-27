continuar = 'S'
n1 = int(input('Digite o 1º Valor: '))
n2 = int(input('Digite o 2º Valor: '))
# print(n1, n2)

while continuar == 'S':
    print('\nSelecione uma opção: ')
    print('[1] SOMA\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] ENCERRAR PROGRAMA\n')
    escolha = int(input())
#SOMA
    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
#MULTIPLICAÇÃO
    if escolha == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
#MAIOR
    if escolha == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        elif n2 > n1:
            print('{} > {}'.format(n2, n1))
        else:
            print('Os dois números são iguais!')
#NOVOS NÚMEROS
    if escolha == 4:
        n1 = int(input('Digite o 1º Valor: '))
        n2 = int(input('Digite o 2º Valor: '))
#ENCERRAR PROGRAMA
    if escolha == 5:
        continuar = 'N'
        print('Obrigado por usar este programa!')
