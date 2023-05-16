v = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        v[0].append(valor)
    else:
        v[1].append(valor)
par = v[0]
impar = v[1]
print(f'Os valores pares ficaram:{sorted(par)}')
print(f'Os valores impar ficaram:{sorted(impar)}')
