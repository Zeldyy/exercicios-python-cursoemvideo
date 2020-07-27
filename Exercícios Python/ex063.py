n = int(input('Digite quantos números da sequência de fibonacci você quer saber: '))
c = 0
if n >= 1: print('{}º termo: {}'.format(c+1, 0))
c += 1
if n >= 2: print('{}º termo: {}'.format(c+1, 1))
c += 1
fibo_atras = 1
fibo_atras_atras = 0
while c != n:
    fibo = fibo_atras_atras + fibo_atras
    print('{}º termo: {}'.format(c+1, fibo))
    fibo_atras_atras = fibo_atras
    fibo_atras = fibo
    c += 1
