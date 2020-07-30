from random import randint
sorteio = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(sorteio)
print(f'Os números gerados são: {sorteio}')
sorteio_ordenado = sorted(sorteio)
print(f'Em ordem fica: {sorteio_ordenado}, com o menor número sendo o {sorteio_ordenado[0]} e maior número o {sorteio_ordenado[4]}')
