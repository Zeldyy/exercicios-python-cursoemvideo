from datetime import datetime
anoatual = datetime.today().year #em que ano estamos
ano = int(input('Digite em que ano você nasceu: ')) #ano de nascimento
idade = anoatual - ano # idade sem considerar os meses
#Comparação
if idade == 18:
    print('Este ano você deve se alistar!')
elif idade >= 18:
    print('Seu tempo de alistamento já passou em {} anos.'.format(idade-18))
else:
    print('Ainda NÃO é hora de se alistar! Faltam {} anos.'.format(18-idade))
