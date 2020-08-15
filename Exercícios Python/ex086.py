matriz = [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'digite o valor {lin, col}: ')))
print('-'*20)
for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^5}]', end='')
    print()
print('-'*20)
