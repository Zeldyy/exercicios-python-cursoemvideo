from datetime import datetime
anoatual = datetime.today().year #em que ano estamos
ano = int(input('Digite em que ano você nasceu: ')) #ano de nascimento
idade = anoatual - ano # idade sem considerar os meses
print('Sua idade é {}, portanto faz parte da '.format(idade), end='')
#Categorias:
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')