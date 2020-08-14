continuar = 'S'
valores = list()
while continuar == 'S':
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} valores.')
print(f'Na ordem decrescente ficam: {valores}')
print('O valor 5 foi digitado.' if 5 in valores else 'O valor 5 não foi digitado.')
