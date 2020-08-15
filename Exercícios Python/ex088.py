from random import randint
from time import sleep
print('-'*50)
print(f'{"JOGO DA MEGA SENA":-^50}')
print('-'*50)
jogos = []
dados = list()
cont_iguais = 0
iguais = False
num_jogos = int(input('Quantos jogos quer que eu sorteie? '))
for c in range(0, num_jogos):
    for d in range(0, 6):  # Sorteio de cada um dos 6 números de cada jogo
        while True:  # Resortear um número se existir valores repetidos sem prejudicar a quantidade de números sorteados
            num = randint(1, 60)
            if d == 0:  # Primeiro valor não precisa de resorteio
                dados.append(num)
                break
            for dado in dados:  # verificação de cada número cadastrado com o novo em análise
                if num == dado:
                    iguais = True
                    cont_iguais += 1  # contador de repetições
                    break
                else:
                    iguais = False
            if iguais is False:  # Se não for igual a nenhum número já cadastrado, num é cadastrado
                dados.append(num)
                break
    dados.sort()  # Ordenamento do jogo em questão
    jogos.append(dados[:])  # Registro na lista composta
    dados.clear()  # Limpeza da lista de teste
for c, j in enumerate(jogos):
    print(f'Jogo {c+1}: {j}')
    sleep(0.1)
print(f'Foram gerados {cont_iguais} números repetidos corrigidos em um mesmo jogo.')
print('-'*50)
print(f'{"BOA SORTE!":-^50}')
print('-'*50)
