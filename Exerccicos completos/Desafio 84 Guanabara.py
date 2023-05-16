dados = []
m = n = contador = 0
while True:
    v = []
    v.append(str(input('Nome: ')))
    v.append(float(input('Peso: ')))
    if contador == 0:
        m = n = v[1]
    else:
        if v[1] > m:
            m = v[1]
        if v[1] < n:
            n = v[1]
    dados.append(v[:])
    contador = contador+1
    a = str(input('Continuar??????')).lower()
    if a == 'n':
        break
print(f'Ao todo você cadastrou {len(dados)} pessoas.')
print(f'Os maiores pesos foram {m}KG, de ', end='')
for p in dados:
    if p[1] == m:
        print(f'{p[0]}', end='')
print()
print(f'Os menores pesos foram {n}KG, de ', end='')
for p in dados:
    if p[1] == n:
        print(f'{p[0]}', end='')
print()
