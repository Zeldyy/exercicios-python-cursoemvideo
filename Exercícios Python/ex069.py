cont = 0
maior_idade = 0
homens = 0
mulher_abaixo20 = 0

while True:
    sexo = 'k' #inicializando variável
    idade = int(input(f'Digite a idade da {cont + 1}ª Pessoa: '))
    while sexo not in 'MF':
        sexo = str(input(f'Digite o sexo da {cont + 1}ª Pessoa: (M/F) ')).strip().upper()[0]
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_abaixo20 += 1
    print(idade, sexo)
    cont += 1
    prosseguir = 'k' #inicializando variável
    while prosseguir not in 'SN':
        prosseguir = str(input('Deseja continuar cadastrando pessoas? (S/N) ')).strip().upper()[0]
    if prosseguir == 'N':
        break
print(f'Foram cadastradas {maior_idade} pessoas maiores de idade, {homens} homens e'
      f' {mulher_abaixo20} mulheres com menos de 20 anos.')
print('Obrigado por utilizar este programa!')
