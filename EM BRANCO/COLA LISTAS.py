lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
lanche.append('cookie')
lanche.insert(0, 'Cachorro quente')
lanche.insert(2, 'outro')
del lanche[4]
lanche.pop(2)  # sem numeração remove o ultimo
lanche.remove('picolé')
print(lanche)

for pos, comida in enumerate(lanche):
    print(f'{comida.upper():.<30} na posição {pos}')


# if algumacoisa in outracoisa:
    # print (algo)
# else:
    # pass (este faz nada)

# valores = [8, 2, 5, 4, 9, 3, 0]
# valores.sort()
# valores.sort(reverse=True)
# print(len(valores))
