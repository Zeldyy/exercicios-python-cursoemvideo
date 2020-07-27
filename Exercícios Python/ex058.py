from random import randint
from time import sleep
print('Vou pensar em um número inteiro de 0 a 10 e você deve tentar adivinhar!')
print('Pensando.', end = '')
sleep(1)
print('.', end = '')
sleep(1)
print('.')
sleep(1)
repetir = 'S'
pensado = randint(0,10)
n_tentativas = 1
print('Pronto!', end = '')
while repetir == 'S':
    tentativa = int(input(' Digite qual número eu pensei: '))
    if pensado == tentativa:
        print('Uau! Você acertou! Foram necessárias {} tentativas.'.format(n_tentativas))
        repetir = 'N'
    else:
        print('Você não acertou! Quer tentar novamente? (S/N) '.format(pensado))
        repetir = str(input()).upper()
        n_tentativas += 1
