b = []
p = []
i = []
while True:
    a = (int(input('Adicione um número aqui: ')))
    b.append(a)
    r = input('Adicionar mais?????? ')
    if a % 2 == 0:
        p.append(a)
    else:
        i.append(a)
    if r == 'n':
        break

print(f'A lista geral ficou assim: {b}')
print(f'A lista dos números pares: {p}')
print(f'A lista dos números ímpares ficou assim: {i}')
