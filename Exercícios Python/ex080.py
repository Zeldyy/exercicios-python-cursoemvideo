valores = list()
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0:
        valores.append(n)
        print('Adicionado ao final da lista.')
    else:
        for cont, p in enumerate(valores):
            if n > p:
                if cont+1 == len(valores):
                    valores.insert(cont+1, n)
                    print('Adicionado ao final da lista.')
                    break
            elif n <= p:
                valores.insert(cont, n)
                print(f'Adicionado na posição {cont} da lista')
                break
print(f'A lista ficou assim: {valores}')
