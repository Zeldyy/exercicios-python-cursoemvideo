altura = float(input('Digite sua  em quilos: '))
peso = float(input('Digite seu peso em metros: '))
imc = peso / (altura ** 2)
#Comparação:
if imc <= 18.5:
    condicao = 'abaixo do peso'
elif 18.5 < imc <= 25:
    condicao = 'com o peso ideal'
elif 25 < imc <= 30:
    condicao = 'com sobrepeso'
elif 30 < imc < 40:
    condicao = 'com obesidade'
else:
    condicao = 'com obesidade mórbida'
print('Você está com o IMC {:.2f} e está {}.'.format(imc, condicao))