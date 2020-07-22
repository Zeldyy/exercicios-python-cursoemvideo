from datetime import datetime
anoatual = datetime.today().year #em que ano estamos
menor = 0
maior = 0
print('Digite o ano de nascimento de 7 pessoas: ')
for c in range(1,8):
    ano = int(input('Digite em que ano a {}ª pessoa nasceu: '.format(c))) #ano de nascimento
    idade = anoatual - ano # idade sem considerar os meses
    if idade >= 18:
        maior += 1
    else:
        menor += 1
    #print(idade) controle
print('{} pessoas são maior de idade.'.format(maior))
print('{} pessoas são menor de idade.'.format(menor))
