from random import randint
from time import sleep
#Algumas declarações
repete = 's'
v = 0 #vitórias
d = 0 #derrotas
r = 0 #rodadas
e = 0 #empates
print('Vamos jogar pedra papel ou tesoura, o famoso JO KEN PO?')
while repete == 's':
      r = r + 1
#Escolha da máquina:
      op = {1: 'PEDRA',
            2: 'PAPEL',
            3: 'TESOURA'}
      maquina = op[randint(1, 3)]
#Escolha do jogador:
      print('=' * 40)
      print('{} RODADA Nº{} {}'.format(20 * '-', r, 20* '-'))
      escolha = str(input('Escolha pedra, papel ou tesoura! ')).strip().upper()
#Tensão no ar...
      print('Verificando', end='')
      sleep(0.8)
      print('.', end='')
      sleep(0.5)
      print('.', end='')
      sleep(0.5)
      print('.')
      sleep(0.8)
      print('Você escolheu {}'.format(escolha), end='')
      sleep(0.8)
      print('.', end='')
      sleep(0.5)
      print('.', end='')
      sleep(0.5)
      print('.')
      sleep(0.8)
      print('Eu escolhi...', end='')
      sleep(0.5)
      print('{}!'.format(maquina))
      sleep(0.8)
      print('=' * 40)
#Quem venceu:
      if escolha == maquina:
            print('\033[1;30;7mEMPATE!\033[m Eu e você escolhemos {}!'.format(escolha.upper()))
            e = e + 1
            print('Você empatou comigo {} vezes!'.format(e))
      elif (escolha == 'PEDRA' and maquina == 'TESOURA') or (escolha == 'TESOURA' and maquina == 'PAPEL') or (escolha == 'PAPEL' and maquina == 'PEDRA'):
            print('Você \033[1;32mVENCEU!\033[m Parabéns! Na próxima eu ganho!')
            v = v + 1
            print('Você me venceu {} vezes e perdeu {} vezes!'.format(v, d))
      elif (escolha == 'PEDRA' and maquina == 'PAPEL') or (escolha == 'TESOURA' and maquina == 'PEDRA') or (escolha == 'PAPEL' and maquina == 'TESOURA'):
            print('HAHA!! Você \033[31;1mPERDEU!\033[m Tente outra vez!')
            d = d + 1
            print('Você me venceu {} vezes e perdeu {} vezes!'.format(v, d))
      else:
            print('Você escreveu algo errado... tente novamente... que sem graça!')
      repete = str(input('Deseja jogar novamente? (s/n) ')).strip().lower()
      print('='*40)
print('Obrigado por jogar! ')
print('Ao todo, você venceu {} vezes, perdeu {} vezes e empatou {} vezes em {} rodadas!'.format(v, d, e, r))
