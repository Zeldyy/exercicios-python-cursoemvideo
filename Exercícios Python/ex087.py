matriz = [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin].append(int(input(f'Digite o valor [{lin},{col}]: ')))
for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^5}]', end='')
    print()
# Análise de Dados:
soma_pares = soma_terceiracoluna = maior_seglin = 0
for lin, linha in enumerate(matriz):
    for c, coluna in enumerate(linha):
        if coluna % 2 == 0:
            soma_pares += coluna
        if c == 2:
            soma_terceiracoluna += coluna
        if lin == 1:
            if coluna > maior_seglin or c == 0:
                maior_seglin = coluna
print(f'{"Análise de Dados":-^50}')
print(f'A soma de todos os valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceiracoluna}')
print(f'O maior valor da segunda linha é {maior_seglin}')
print('-'*50)
