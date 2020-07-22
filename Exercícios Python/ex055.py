menorpeso = 1000
maiorpeso = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
print('Os maior peso lido foi {}Kg e o menor peso foi {}Kg.'.format(maiorpeso, menorpeso))