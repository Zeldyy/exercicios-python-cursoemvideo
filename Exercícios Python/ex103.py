def ficha(jogador='<desconhecido>', gols=0):
    """
    -> recebe dois parâmetros opcionais e retorna os valores, e cria uma mensagem padrão se não receber a informação correta.
    :param jogador: recebe um string com o nome do jogador
    :param gols: recebe a quantidade de gols do jogador (string que é transformada em integer)
    :return: retorna dois parâmetros em uma tupla: o nome do jogador e a quantidade de gols, devidamente corrigida.
    """
    if jogador == '':
        jogador = '<desconhecido>'
    if gols.isnumeric() == False:
        gols = 0
    int(gols)
    return jogador, gols

nome = str(input('Nome do jogador: '))
gol = str(input('Quantidade de gols: '))
print(f'O jogador {ficha(nome, gol)[0]} marcou {ficha(nome, gol)[1]} gol(s).')
