somaidade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulher_under20 = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª Pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª Pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª Pessoa (m/f): '.format(c))).lower()
    somaidade += idade
    if sexo == 'm' and idade > idade_homem_mais_velho:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    if sexo == 'f' and idade < 20:
        mulher_under20 += 1

mediaidade = somaidade / 4
print('A média da idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho é o {} e sua idade é de {} anos.'.format(nome_homem_mais_velho, idade_homem_mais_velho))
print('Existem {} mulheres com menos de 20 anos.'.format(mulher_under20))