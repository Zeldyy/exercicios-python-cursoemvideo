n = int(input('Digite quantos números quer gravar: '))
for c in range(0,n):
    g[c] = int(input('Digite o {}º valor: '.format(c)))
print(g)