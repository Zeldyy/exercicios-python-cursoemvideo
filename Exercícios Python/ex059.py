escolha = 9
n1 = int(input('Digite o 1º Valor: '))
n2 = int(input('Digite o 2º Valor: '))
# print(n1, n2)

while escolha != 5:
    print('\nSelecione uma opção: ')
    print('[1] SOMA\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4] NOVOS NÚMEROS\n'
          '[5] ENCERRAR PROGRAMA\n')
    escolha = int(input())
    if escolha == 1: #SOMA
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif escolha == 2: #MULTIPLICAÇÃO
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif escolha == 3: #MAIOR
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        elif n2 > n1:
            print('{} > {}'.format(n2, n1))
        else:
            print('Os dois números são iguais!')
    elif escolha == 4: #NOVOS NÚMEROS
        n1 = int(input('Digite o 1º Valor: '))
        n2 = int(input('Digite o 2º Valor: '))
    elif escolha == 5: #ENCERRAR PROGRAMA
        print('Obrigado por usar este programa!')
    else:
        print('Opção Inválida')
