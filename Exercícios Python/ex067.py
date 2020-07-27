print('Programa que lê tabuadas. Digite um número negativo para encerrar o programa.')
while True:
    n = int(input('Digite um valor: '))
    if n < 0:
        break
    print('-' * 20)
    for c in range(1,11):
        print(f'{n:3} x {c:3} = {n*c:4}')
    print('-' * 20)
print('Obrigado por utilizar o programa!')