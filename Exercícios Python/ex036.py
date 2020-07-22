print('Empréstimo bancário para comprar imóveis!\nSeja bem vindo!')
valorcasa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

# Prestações
prestacoesmensais = valorcasa / (anos*12)

# Verificação
if prestacoesmensais > salário * 0.3:
    print('Infelizmente seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado!', end ='')
    print('O valor das prestações será de R${:.2f}.'.format(prestacoesmensais))