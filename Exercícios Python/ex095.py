cadastro = list()
while True:
  jogador = {'nome': str(input('Nome do Jogador: ')).strip(),
            'partidas': int(input('Quantas partidas ele jogou? ')),
            'gols': [],
            'totalgols': 0}
  for jogo in range(0, jogador['partidas']):
    jogador['gols'].append(int(input(f'Gols na partida {jogo+1}: ')))
    jogador['totalgols'] += jogador['gols'][jogo]
  cadastro.append(jogador)
  cont = str(input('Deseja continuar? (S/N): ')).strip()[0]
  if cont in 'Nn':
    break
# Painel geral
print(f'No   Nome         Gols         Total')
for n, jogador in enumerate(cadastro):
  print(f'{n+1:<4}{jogador["nome"]:<12}{str(jogador["gols"]):<13}{jogador["totalgols"]:>4}')
# Informações detalhadas
while True:
  num = int(input(f'Número do jogador que deseja saber detalhes (999 = cancelar): '))
  if num == 999:
    break
  if num-1 < len(cadastro) and num-1 >= 0:
      print(f'Levantamento do jogador {cadastro[num-1]["nome"]}:')
      for n, gols in enumerate(cadastro[num-1]['gols']):
        print(f'No jogo {n+1} fez {gols} gols.')
