def titulo(txt):
    comp = len(txt) + 4
    print('-' * comp)
    print(f'  {txt}  ')
    print('-' * comp)
def maior(* num):
    titulo(f'Maior valor entre {num}')
    print(f'O maior valor é {max(num)}')
    print('-' * 30)


maior(2, 4, 8, 1, 5, 7, 2, 4)
maior(0, 4, 9)
maior(5, 3, 0, -1, -10)
