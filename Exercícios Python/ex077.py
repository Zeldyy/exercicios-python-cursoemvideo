palavras = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
for pal in palavras:
    print(f'Na palavra {pal} temos as vogais: ', end = '')
    '''for c in range(0, len(pal)):
        print(pal[c])'''
    for c in pal:
        if c in 'aeiou':
            print('', c, '', end = '')
    print()
