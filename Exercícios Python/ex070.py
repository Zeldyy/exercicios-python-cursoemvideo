print('=== Programa de leitura de compras ===')
cont = 0
gastos = 0
milmais = 0
mais_barato = ''
preco_barato = 0
while True:
    nome = str(input(f'Nome do {cont + 1}º Produto: ')).strip().lower().capitalize()
    preco = float(input(f'Preço da {nome}: R$'))
    cont += 1
    if cont == 1:
        mais_barato = nome
        preco_barato = preco
    elif preco < preco_barato:
        mais_barato = nome
        preco_barato = preco
    if preco > 1000:
        milmais += 1
    gastos += preco
    prosseguir = str(input('Continuar? (S/N) ')).strip().lower()[0]
    if prosseguir == 'n':
        break
print(f'======================='
      f'Estatísticas:\n'
      f'Foram gastos R${gastos:.2f} ao total\n'
      f'{milmais} produtos custaram mais de R$1000.00\n'
      f'{mais_barato} foi o produto mais barato, custando R${preco_barato:.2f}\n'
      f'=======================')
print('Obrigado por utilizar o programa!')
