num = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha para que base de conversão quer converter este número. \n'
                    '1: Binário \n'
                    '2: Octal \n'
                    '3: Hexadecimal\n'))
if escolha == 1:
    print('O número em binário é: {}'.format(bin(num)[2:]))
elif escolha == 2:
    print('O número em Octal é: {}'.format(oct(num)[2:]))
elif escolha == 3:
    print('O número em Hexadecimal é: {}'.format(hex(num)[2:]))
else:
    print('Escolha uma opção válida para o programa!')

