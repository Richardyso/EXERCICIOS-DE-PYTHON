total = acima100 = cont = menor = 0
barato = ''
respectivo = None


while True:
    nome = str(input('Qual o nome do Item?'))
    preco = float(input('Quanto custa? R$'))
    cont = cont+1
    total = total+preco

    if preco > 100:
        acima100 = acima100+1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
        else:
            if preco < menor:
                menor = preco
                barato = nome
    cc = str(input('Deseja adicionar mais itens?'))
    if cc == 's':
        continue
    else:
        break

print(f'Produto mais de 100 Reias: R${acima100}')
print(f'Total gasto foi: R$ {total:5.2f}')
print(f'O item mais barato foi {barato} e custou R$ {menor:2}')
