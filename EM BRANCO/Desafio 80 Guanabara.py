i = []
i1 = []
for x in range(0, 5):
    i.append(int(input('Digite um número: ')))
print(f'Lista Original=  {i}')
z = min(i)
c = max(i)
i.remove(z)
s = min(i)
i.remove(c)
q = max(i)

i1.append(z)
i1.append(s)
i1.append(i[0])
i1.append(q)
i1.append(c)
print(i1)

# TENTEI ASSIM TBM MAS NAO DEU
i = []
i1 = []
i2 = []
for x in range(0, 5):
    i.append(int(input('Digite um número: ')))
print(f'Lista Original=  {i}')
z = min(i)
c = max(i)
if i2 > z and i2 < c:
    t = min(i2)
    m = max(i2)
i1.insert(0, z)
i1.insert(1, min(i2))
i1.insert(2, t)
i1.insert(3, m)
i1.insert(4, c)
print(i1)
