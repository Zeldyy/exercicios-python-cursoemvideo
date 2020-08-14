expressao = str(input('Digite uma expressão com parêntesis: ')).strip().lower()
parent_inicial = 0
pos_inicial = []
parent_final = 0
pos_final = []
erro = False
for pos, c in enumerate(expressao):
    if '(' in c:
        parent_inicial += 1
        pos_inicial.append(pos)
    elif ')' in c:
        parent_final += 1
        pos_final.append(pos)
''' Prints usados para teste do programa:
print(parent_inicial)
print(pos_inicial)
print(parent_final)
print(pos_final)'''
if parent_inicial != parent_final:
    erro = True
else:
    for c in range(0, len(pos_inicial)):
        if pos_inicial[c] > pos_final[c]:
            erro = True
            break
if erro is True:
    print('A expressão contém um erro nos parêntesis!')
else:
    print('A equação está com os parêntesis corretos!')
