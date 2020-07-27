print('='*20, 'CAIXA ELETRÔNICO', '='*20)
print('Cédulas Disponíveis: R$50, R$20, R$10 e R$1.')
n = int(input('Qual valor deseja sacar? '))
separar = n
c50 = 0
c20 = 0
c10 = 0
c1 = 0
#segmentação
if separar >= 50:
    c50 = separar // 50
    separar = separar % 50
if separar >= 20:
    c20 = separar // 20
    separar = separar % 20
if separar >= 10:
    c10 = separar // 10
    separar = separar % 10
if separar >= 1:
    c1 = separar
print('Cédulas sacadas:')
if c50 > 0:
    print(f'{c50} notas de 50;')
if c20 > 0:
    print(f'{c20} notas de 20;')
if c10 > 0:
    print(f'{c10} nota de 10;')
if c1 > 0:
    print(f'{c1} notas de 1.')
print('='*58)
