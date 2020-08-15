cadastro = list()
aluno = list()
notas = list()
while True:
    aluno.append(str(input('Nome: ')).strip())
    for c in range(0, 2):
        notas.append(float(input(f'Nota {c+1}: ')))
    aluno.append(notas[:])
    aluno.append((notas[0] + notas[1])/2)
    notas.clear()
    cadastro.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja continuar? (S/N) ')).strip().lower()[0]
    if continuar in 'Nn':
        break
print(f'{"BOLETIM":-^30}')
for c, aluno in enumerate(cadastro):
    print(f'CAD: {c}, Nome: {aluno[0]:<10} ->  Média: {aluno[2]:.1f}')
# print(cadastro)
print('-'*30)
while True:
    cad = int(input('Digite o CAD de um aluno para verificar notas individuais: (999 -> CANCELA) '))
    if cad == 999:
        break
    if cad <= len(cadastro) - 1:
        print(f'As notas de {cadastro[cad][0]} são {cadastro[cad][1]}')
print(f'{"VOLTE SEMPRE!":-^30}')
