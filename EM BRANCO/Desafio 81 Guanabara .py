l = []
while True:
    l.append(int(input('Adicione um valor: ')))
    r = input('Quer adicionar mais??? ')
    if r == 's':
        pass
    else:
        break
print(f'A quantidade de itens digitados foi: {len(l)}')
print(f'A ordem da lista decrescente ficou assim: {sorted(l, reverse=True)}')
if 5 in (l):
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 NÃO foi digitado')
