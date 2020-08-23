def titulo(txt):
    """
    -> Imprime em formato de título.
    :param txt: texto para título.
    """
    print('-' * 40)
    print(f'{txt:^40}')
    print('-' * 40)


def leiaint(txt):
    """
    -> Lê número inteiro com tratamento de erros.
    :param txt: prompt do input.
    """
    while True:
        try:
            a = int(input(txt).strip())
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um valor.')
            a = 0
            break
        except Exception as erro:
            print(f'O seguinte erro aconteceu: {erro.__class__}.\nDigite um número inteiro.')
        else:
            break
    return a


def leiafloat(txt):
    """
    -> Lê número real com tratamento de erros.
    :param txt: prompt do input.
    """
    while True:
        try:
            a = float(input(txt).strip().replace(',', '.'))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar um valor.')
            a = 0
            break
        except Exception as erro:
            print(f'O seguinte erro aconteceu: {erro.__class__}. Digite um número real.')
        else:
            break
    return a
