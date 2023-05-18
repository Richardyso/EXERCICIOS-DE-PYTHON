v = []
for c in range(5):
    v.append(int(input(f'Digite um valor para posição {c}: ')))
# print(f'Os valores digitados foram: {v}')
    m = max(v)
    n = min(v)
print(f'O maior valor foi: {m} localizado na posição ', end='')
for i, x in enumerate(v):
    if v[i] == m:
        print(i)
print()
print(f'O menor valor foi: {n} localizado na posição ', end='')
for i, x in enumerate(v):
    if v[i] == n:
        print(i)
print()
