m = 0
for c in range(0, 7):
    a = int(input('Ano de nascimento: '))
    i = 2023-a
    if i >= 21:
        m = m+1
print('Total maior de idade é: {}'.format(m))
