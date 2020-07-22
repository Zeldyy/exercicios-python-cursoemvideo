n = int(input('Digite o primeiro termo de uma P.A: '))
r = int(input('Digite a razão da P.A: '))
print('Os 10 primeiros termos dessa razão são: ')
for c in range(n, n + 10 * r, r):
    print(c)