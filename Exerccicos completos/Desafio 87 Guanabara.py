m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = []
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor: [{l}, {c}]'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]}]', end='')

    print()

if m[0][0] % 2 == 0:
    p.append(m[0][0])
if m[0][1] % 2 == 0:
    p.append(m[0][1])
if m[0][2] % 2 == 0:
    p.append(m[0][2])
if m[1][0] % 2 == 0:
    p.append(m[1][0])
if m[1][1] % 2 == 0:
    p.append(m[1][1])
if m[1][2] % 2 == 0:
    p.append(m[1][2])
if m[2][0] % 2 == 0:
    p.append(m[2][0])
if m[2][1] % 2 == 0:
    p.append(m[2][1])
if m[2][2] % 2 == 0:
    p.append(m[2][2])
print(f'A soma de todos números pares digitados foi: {sum(p)}')

c1 = (m[0][2])
c2 = (m[1][2])
c3 = (m[2][2])
print(f'A soma dos itens da coluna 3 foram: {c1+c2+c3}')

ll = max(m[1][0], m[1][1], m[1][2])
print(f'O maior valor da segunda linha foi: {ll}')
# coluna1=m[[0][0]]
# coluna2=m[[0][1]]
# coluna3=m[[0][2]]

# l1 = (m[0][0] + m[0][1] + m[0][2])
# l2 = (m[1][0] + m[1][1] + m[1][2])
# l3 = (m[2][0] + m[2][1] + m[2][2])
# print(f'A soma de todos valores digitados foi: {l1+l2+l3}')
