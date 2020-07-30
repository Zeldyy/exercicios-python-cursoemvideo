valores = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
           int(input('Digite outro número: ')), int(input('Digite o último número: ')))
print(valores)
print(f'Você digitou o número 9 -> {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O número 3 aparece na {valores.index(3)+ 1}ª posição ')
else:
    print(f'O número 3 não aparece nos números')
print(f'O números pares foram: ', end = '')
for c in range(0, 4):
    if valores[c] % 2 == 0:
        print(valores[c],'', end = '')
