frase = str(input('Digite uma frase e direi se é ou não um palíndromo: \n').lower().strip())
#print(frase) controle 1
frase_split = frase.split()
#print(frase_split) controle 2
frase_junta = ''.join(frase_split)
#print(frase_junta) controle 3
n = len(frase_junta)
#print(n) controle 4
frase_reversa = ''
for c in range(n-1, -1, -1):
    frase_reversa += frase_junta[c]
#print(frase_reversa) controle 5
if frase_reversa == frase_junta:
    print('Esta frase é um palíndromo!!')
else:
    print('Esta frase não é um palíndromo!!')