n = []
p = []
x = ''
while True:
    n.append(input('Qual o nome do Item?'))
    p.append(float(input('Quanto custa? R$')))
    add = input('Adicionar mais?? [s/n]').lower()
    if add == 'n':
        break
t = sum(p)
for nome, preco in zip(n, p):
    if preco > 100:
        x = nome
        pr = preco
print(f'Produto mais de 100 Reias: R${x}')
print(f'Total gasto foi: R$ {t}')
print(f'O item mais barato foi {nome} e custou R$ {pr}')
