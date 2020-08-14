numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
continuar = 's'
cont = 0
while continuar == 's':
    while True:
        n = int(input('Digite um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        else:
            print('Digite novamente. ', end = '')
    #for num, extenso in enumerate(numeros):
    #    print(num, extenso)
    print(f'Você digitou o número {numeros[n]}.')
    continuar = str(input('Quer continuar? (S/N) ')).lower().strip()[0]
    cont += 1
print(f'Obrigado por utilizar este programa! Você consultou {cont} números.')
