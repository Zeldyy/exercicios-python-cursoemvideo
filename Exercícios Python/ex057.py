sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo? (M/F) ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F': print('Por favor digite M ou F')
print(sexo)
