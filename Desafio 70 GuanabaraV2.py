itens = []
precos = []
alto = []
baixo = []
p = []
# print(f{= ^ 16}'MERCADÃO DO PARAIBA'{= ^ 16})
print(f"{'='*16}MERCADÃO DO PARAIBA{'='*16}")
c = str(input('Quer começar? '))
while c[0].lower() == 's' or 'v' or 'o':
    i = str(input('Qual nome do item? '))
    p = int(input('Quanto ele custa? '))
    # PARÂMETROS
    itens.append(i)
    precos.append(p)
    if p <= 9:
        baixo.append(p)
    else:
        alto.append(p)
    acima = len(alto)
    # VALIDAÇÕES
    total = sum(precos)
    barato = min(precos)
    # vai armazenar qual dos precos é o mais barato
    mbarato = precos.index(barato)
    ibarato = itens[mbarato]  # ibarato recebe qual dos itens é mbarato
# ESTUDAR MÉTODO INDEX
    # MAIS?
    a = str(input('Quer adicionar mais? '))

    # FINALIZAÇÃO
    if a[0].lower() == 's':
        continue
    elif a[0].lower() == 'n':
        break
    else:
        print("Resposta inválida. Por favor, digite 's' ou 'n'.")
    # ARÉA DE PRINTS
print(f'A quantidade de produtos acima de 10 reais foi {acima}!')
print(f'O item mais barato é {ibarato}!')
print(f'O valor gasto total foi R$ {total}!')
