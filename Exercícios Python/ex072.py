numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= int(n) <= 20:
        break
    else:
        print('Digite novamente. ', end = '')
#for num, extenso in enumerate(numeros):
#    print(num, extenso)
print(f'Você digitou o número {numeros[n]}.')
