l = []
idd = []
while True:
    d = {}
    n = str(input('Nome: ')).capitalize()
    s = str(input('Sexo: ')).lower()
    i = int(input('Idade: '))
    d = {'nome': n, 'sexo': s, 'idade': i}
    l.append(d)
    idd.append(i)
    ct = str(input('Continuar? ')).lower()
    if ct == 'n':
        break
m = sum(idd)/len(l)
mulheres = []
for pessoa in l:
    if pessoa["sexo"] == 'f':
        mulheres.append(pessoa)
acimamedia = []
for pessoa in l:
    if pessoa["idade"] > m:
        acimamedia.append(pessoa["nome"])


print('-=' * 30)
print(f'Foram cadastrados {len(l)} pessoas')
print(f'A média de idade dos cadastrados foram: {m:.1f} anos')
print(f'O nome das mulheres foram: {mulheres}')
print(f'As pessoas acima da média de idade foram: {acimamedia}')
