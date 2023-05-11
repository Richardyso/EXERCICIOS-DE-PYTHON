v = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in v:
        print('Esse número já foi digitado, tente outro.')
    else:
        v.append(valor)
        print('Adicionado com sucesso!')
    r = str(input('Quer adicionar mais? '))
    r = r.lower()
    if r[0] != 's':
        break
print(f'Os valores digitados em ordem crescente ficaram assim: {sorted(v)}')
