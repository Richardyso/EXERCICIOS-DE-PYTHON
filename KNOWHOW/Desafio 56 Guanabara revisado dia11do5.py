p = []
i = []
s = []
x = []
id = []
f = []
completo = []
for c in range(0, 4):
    p.append(input('Adicione aqui o nome da pessoa : '))
    i.append(int(input('Qual a idade dessa pessoa? ')))
    s.append(input('Qual o sexo dessa pessoa? [m/f]').lower())
m = sum(i)/len(i)
for sexo, idade, nome in zip(s, i, p):
    if sexo == 'm':
        id = i.index(max(i))
        v = p[id]
for sexo, idade in zip(s, i):
    if sexo == 'f' and idade < 20:
        x.append(sexo)

print(f'A idade média das pessoas ficou em: {m} anos')
print(f'O homem mais velho se chama: {v}')
print(f'A quantidade de mulheres abaixo de 20 anos foi: {len(x)}')
