total = 0
precos = []
item = []
respectivo = None


while True:
    nome = str(input('Qual o nome do Item?'))
    preco = float(input('Quanto custa?'))
    total = total+preco

    # item.append(nome, preco)

    if preco >= 100:
        precos.append(preco)
    # elif preco == min(item):
    #     respectivo = nome
    cc = str(input('Deseja adicionar mais itens?'))
    if cc == 's':
        continue
    else:
        break

# print(f'O Produto mais barato foi: {respectivo}')
print(f'Produto mais de 100 Reias: {precos}')
print(f'Total gasto foi: R$ {total}')
