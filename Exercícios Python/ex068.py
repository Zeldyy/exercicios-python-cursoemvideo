from random import randint
print('Programa que joga par ou ímpar com o jogador! Encerra quando você perde.')
vitorias = 0
while True:
    jogador = str(input('Escolha par ou impar: (P/I) ')).strip().upper()[0]
    num_jogador = int(input('Escolha um número inteiro: '))
    #computador
    num_computador = randint(0, 10)
    if jogador == 'P':
        escolha_comp = 'I'
    else:
        escolha_comp = 'P'
    print(f'Eu escolho {num_computador}!')
    #verificação
    soma = num_jogador + num_computador
    if soma % 2 == 0:
        if jogador == 'P':
            print(f'A soma deu {soma}. Parabéns! Você venceu!')
            vitorias += 1
        elif jogador == 'I':
            print(f'A soma deu {soma}. Você perdeu! Você ganhou {vitorias} vezes.')
            break
    else:
        if jogador == 'I':
            print(f'A soma deu {soma}. Parabéns! Você venceu!')
            vitorias += 1
        elif jogador == 'P':
            print(f'A soma deu {soma}. Você perdeu! Você ganhou {vitorias} vezes.')
            break
print('Obrigado por jogar!')