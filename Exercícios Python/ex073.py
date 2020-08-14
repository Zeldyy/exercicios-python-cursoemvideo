times = ('Athletico PRA', 'Atlético Goianiense', 'Atlético MG',
         'Bahia', 'Botafogo', 'Ceará', 'Corinthians', 'Coritiba',
         'Flamengo', 'Fluminense', 'Fortaleza EC', 'Goiás', 'Grêmio',
         'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'Sport',
         'São Paulo', 'Vasco da Gama')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os cinco últimos são: {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O Bahia está na {times.index("Bahia")+1}ª Posição')

'''for c in range(0, 5):
    print(f'O {c+1}º colocado é: {times[c]}')
print('='*30)
print(f'Os 4 últimos são:')
for c in range(-1, -5, -1):
    print(f'{times[c]}')
print('=' * 30)
print('Times em ordem alfabética: ')
times_organizados = sorted(times)
for c in range(0, 20):
    print(times_organizados[c])
print('=' * 30)
for pos in range(0, 20):
    if times[pos] == 'Bahia':
        print(f'A posição do Bahia é a {pos + 1}ª posição.')'''
