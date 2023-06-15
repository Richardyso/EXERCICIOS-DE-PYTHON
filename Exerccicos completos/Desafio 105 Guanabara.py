def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações
    :param n: uma ou mais notas
    :param sit: Valor opcional
    :return: Dicionário com valores
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 4 and r['média'] >= 6:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


##
resp = notas(5.5, 3.5, 9.5, sit=True)
print(resp)
help(notas)