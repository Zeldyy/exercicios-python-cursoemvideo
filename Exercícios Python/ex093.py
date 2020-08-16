jogador = {'nome': str(input('Nome do Jogador: ')).strip(),
           'partidas': int(input('Quantas partidas ele jogou? ')),
           'gols': [],
           'totalgols': 0}
for jogo in range(0, jogador['partidas']):
  jogador['gols'].append(int(input(f'Gols na partida {jogo+1}: ')))
  jogador['totalgols'] += jogador['gols'][jogo]
# Solução 1
print(jogador)
# Solução 2
for chave, valor in jogador.items():
  print(f'O campo {chave} tem valor {valor}.')
# Solução 3
print(f'O jogador {jogador["nome"]} fez um total de {jogador["partidas"]} partidas.')
for c, v in enumerate(jogador['gols']):
  print(f'=> Na partida {c+1} o jogador fez {v} gols.')
print(f'Foi um total de {jogador["totalgols"]} gols.')
