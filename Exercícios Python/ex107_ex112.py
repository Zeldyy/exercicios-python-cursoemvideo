"""Modulo moeda

Série de funções que trabalham com moedas, exercício ex107 do curso de python em Curso em Vídeo.
"""
def dobro(x, formato=False):
    """
    -> Retorna dobro de um valor.
    :param x: valor.
    :param formato: se True formata para R$
    """
    if formato is True:
        return moeda(2 * x)
    else:
        return 2 * x


def metade(x, formato=False):
    """
    -> Retorna metade de um valor
    :param x: valor.
    :param formato: se True formata para R$
    """
    if formato is True:
        return moeda(x / 2)
    else:
        return x / 2


def aumentar(x, p, formato=False):
    """
    -> Retorna valor aumentado de porcentagem
    :param x: valor a ser aumentado.
    :param p: porcentagem em % a ser aumentado
    :param formato: se True formata para R$
    """
    if formato is True:
        return moeda(x * (1 + p / 100))
    else:
        return x * (1 + p / 100)


def diminuir(x, p, formato=False):
    """
    -> Retorna valor diminuido de porcentagem
    :param x: valor a ser diminuido.
    :param p: porcentagem em % a ser diminuido
    :param formato: se True formata para R$
    """
    if formato is True:
        return moeda(x * (1 - p / 100))
    else:
        return x * (1 - p / 100)


def moeda(txt):
    """
    -> Adiciona formato monetário nos valores emitidos.
    """
    return f'R${txt:.2f}'


def resumo(valor, pa, pd):
    """
    -> Cria um aparato geral com uso de todas as funções do módulo.
    :param valor: valor em reais para ser trabalhado.
    :param pa: porcentagem para aumento do valor.
    :param pd: porcentagem para diminuição do valor.
    """
    print('-' * 30)
    print(f'{"RESUMO DE MOEDA.PY":^30}')
    print('-' * 30)
    print(f'Valor analisado:  {moeda(valor):<10}')
    print(f'Dobro do valor:   {dobro(valor, True):<10}')
    print(f'Metade do valor:  {metade(valor, True):<10}')
    print(f'{pa}% de aumento:   {aumentar(valor, pa, True):<10}')
    print(f'{pd}% de redução:   {diminuir(valor, pd, True):<10}')
    print('-' * 30)


def leiadinheiro(texto):
    """
    -> Função que valida um dado recebido para somente aceitar valores númericos.
    :param texto: texto para usar no input.
    """
    while True:
        num = input(texto)
        if ',' in num and '.' in num:
            None
        elif num.replace('.', '1', 1).replace(',', '2', 1).isnumeric() is True:
            return float(num.replace(',', '.'))
            break
        print('Erro! Digite um valor monetário.')
 
