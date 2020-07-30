lista = ('Lápis', 2, 'Papel', 5, 'Plantas', 22.5, 'Pano de Chão', 9.9, 'Jujubas', 4, 'Serenata de Amor', 8)
print(lista)
print('-'*55)
print(' '*17, 'LISTAGEM DE PREÇOS', ' '*10)
print('-'*55)
for c in range(0,12,2):
    print(f'{lista[c]:.<40}R${lista[c+1]:7.2f}')
print('-'*55)
