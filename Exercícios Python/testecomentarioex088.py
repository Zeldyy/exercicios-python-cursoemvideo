from random import sample as s
[print(j) for j in (sorted(s(range(1, 61), 6)) for n in range(int(input('\nPalpites: '))))]