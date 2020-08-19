from random import randint
def titulo(txt):
    comp = len(txt) + 4
    print('-' * comp)
    print(f'  {txt}  ')
    print('-' * comp)
def sorteio():
    lista = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
    return lista
def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma



valores = sorteio()
print(f'Os valores sorteados foram {valores} e a soma dos números pares é {somaPar(valores)}')
