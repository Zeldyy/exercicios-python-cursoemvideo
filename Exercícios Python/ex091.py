'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from operator import itemgetter
'''
O itemgetter foi usado neste programa para conseguir ordenar dados oriundos
de um dicionário, usando a função sorted(), como demonstrado abaixo.
'''
jogo = {}
ordenado = dict()  #mesma coisa que {}
# Criando um dicionário com chaves variáveis.
for c in range(0, 4):
  jogo[f'jogador{c+1}'] = randint(1, 6)
# Imprimindo sorteios.
for chave, valor in jogo.items():
    print(f'O {chave} tirou {valor}')
# Criando uma lista com os valores ordenados de um dicionário por pares em tuplas.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'Para estudo: {ranking}')  #Para deixar claro como fica o formato da lista com tuplas internas depois de ordenado.
# Organizando so valores em um dicionário.
for tuplas in ranking:
  ordenado[tuplas[0]] = tuplas[1]
print(f'Para estudo: {ordenado}')  #Para deixar claro como ficou após organização em dicionário.
# Imprimindo dicionário ordenado.
print('-' * 30)
c = 0
for chave, valor in ordenado.items():
  print(f'Em {c+1}º lugar: {chave} com {valor}.')
  c += 1
