nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1+nota2)/2
print('Sua média foi {}'.format(media))
#Comparação
if media < 5.0:
    print('Precisa estudar mais, está reprovado...')
elif 5.0 <= media < 6.9:
    print('Está em recuperação.')
else:
    print('Parabéns! Está aprovado!')
