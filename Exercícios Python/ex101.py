from datetime import datetime
def voto(nascimento):
    """
    Função voto
    """
    global idade
    idade = datetime.now().year - nascimento
    if idade < 16:
        v = 'NEGADO'
    elif 18 > idade > 16 or idade >= 65:
        v = 'OPCIONAL'
    elif 64 > idade >= 18:
        v = 'OBRIGATÓRIO'
    return v

ano = datetime.now().year
nasc = int(input('Digite o ano de nascimento: '))
print(f'Com a idade {ano - nasc} o voto é {voto(nasc)}')
