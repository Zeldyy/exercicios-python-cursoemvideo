def notas(* valoresnotas, situação=False):
    """
    -> Lê notas e retorna um dicionário com características delas.
    :param notas: várias notas em uma lista, tupla ou valores em série.
    :param situação: se True, irá dizer como está a situação do aluno entre RUIM, RAZOÁVEL e BOA.
    :return: dicionário com quantidade de notas, maior nota, menor nota, média das notas e situação se True.
    """
    soma = 0
    for notas in valoresnotas:
        soma += notas
    media = soma / len(valoresnotas)
    dicionario = {'total': len(valoresnotas), 'maior': max(valoresnotas), 'min': min(valoresnotas), 'média': media}
    if situação is True:
        if media < 5:
            dicionario['situação'] = 'RUIM'
        if 7 > media >= 5:
            dicionario['situação'] = 'RAZOÁVEL'
        if media >= 7:
            dicionario['situação'] = 'BOA'
    return dicionario


resp = notas(5.5, 9.3, 7.6, 5.9, 5.3, 9.6, situação=True)
print(resp)
print(help(notas))
