def ajuda(texto):
    titulo(f'Buscando pelo manual de {texto}')
    print(cores['verde'], end='')
    help(texto)
    print('\033[m', end='')
def titulo(txt, a='ciano'):
    print(cores[a], end='')
    comp = len(txt) + 4
    print('-' * comp)
    print(f'  {txt}  ')
    print('-' * comp, end='')
    print(cores['semcor'])


cores = {'preto': f'\033[1;37;40m',
         'semcor': f'\033[m',
         'ciano': f'\033[1;31;46m',
         'amarelo': f'\033[7;1;31;43m',
         'verde': f'\033[30;42m'}
titulo('Sistema de ajuda interativa de Python', 'preto')
while True:
    titulo('Digite o comando ou biblioteca que deseja pesquisar (fim encerra):', 'preto')
    escolha = str(input()).lower()
    if escolha == 'fim':
        break
    ajuda(escolha)
titulo('Obrigado por usar a ajuda interativa de Python', 'preto')  
