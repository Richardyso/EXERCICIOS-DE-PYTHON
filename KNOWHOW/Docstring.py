def contador(i, f, p):
    """
    Teste de docstring
    :param: Inicio da contagem
    :paramf: Final da contagem
    :paramp: Passo da contagem
    :return: sem retorno
    """
    c = 0
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim')


contador(1, 22, 3)
