def titulo(txt):
    comp = len(txt) + 4
    print('-' * comp)
    print(f'  {txt}  ')
    print('-' * comp)
def area(a, b):
    titulo('Área de Terreno')
    print(f'A área do terreno com as dimensões {a:3.2f} x {b:3.2f} m é {a*b:3.2f} m²')


# Programa Principal
titulo('Dimensões do Terreno')
a = float(input('Digite a largura (m): '))
b = float(input('Digite o comprimento (m): '))
area(a, b)
