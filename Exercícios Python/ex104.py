def leiaint(txt):
    while True:
        a = input(txt)
        if a.isnumeric():
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro.\033[m')
    return int(a)


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')
