valor = float(input('Digite o preço normal do produto: R$'))
pgt = int(input('''Qual a condição de pagamento:
(1) Dinheiro/Cheque
(2) À vista no cartão
(3) Em até 2x no cartão
(4) 3x ou mais no cartão\n'''))
#condições:
if pgt == 1:
    print('Concedemos nesta opção 10% de desconto,\nficando de R${:.2f} por R${:.2f}!'.format(valor, valor*0.9))
elif pgt == 2:
    print('Concedemos nesta opção 5% de desconto,\nficando de R${:.2f} por R${:.2f}!'.format(valor, valor * 0.95))
elif pgt == 3:
    print('Não concedemos desconto nesta opção, ficando R${:.2f}.'.format(valor))
elif pgt == 4:
    print('Nesta opção cobramos 20% de juros,\nficando de R${:.2f} por R${:.2f}!'.format(valor, valor * 1.2))
else:
    print('Condição inválida, tente novamente.')