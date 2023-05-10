desenho = ('-'*40)
print(desenho)
print(f'{"Listagem de preços!":^40}')
print(desenho)
lista = ('Pão', 1, 'Cuscuz', 3.9, 'Suco', 6.5, 'Kitut',
         10, 'Fone de Ouvido', 100, 'Perfume', 200)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>7.2f}')
print(desenho)
