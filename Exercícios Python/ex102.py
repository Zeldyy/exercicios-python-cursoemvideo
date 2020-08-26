def fatorial(num, show=False):
    """
    -> imprime fatorial de um número e seu processo de cálculo se requisitado
    :param num: inteiro que será calculado o fatorial
    :param show: se True irá mostrar a equação do cálculo.
    :return: valor do fatorial do num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show is True:
        for c in range(num, 0, -1):
            print(f'{c}', end=' ')
            print(f'x ' if c > 1 else '= ', end = '')
    return f


# Programa Principal
fatorial(8, True)
help(fatorial)
