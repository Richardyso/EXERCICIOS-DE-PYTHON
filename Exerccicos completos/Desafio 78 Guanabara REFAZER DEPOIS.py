#ANTES DO EXERCÍCIO 78 FAZER LISTA EM ORDEM SEM A FUNÇÃO SORTED PARA TREKNAR A LÓGICA
# lista = [5, 2, 7, 6, 1]
# lista.insert(0, lista[4])
# lista.pop(5)

# lista.insert(1, lista[2])
# lista.pop(3)
# #
# lista.insert(3, lista[4])
# lista.pop(5)

# print(lista)


#EXERCÍCIO 78 COMENTADO PELO CHATGPT

listanum = []  # cria uma lista vazia chamada listanum
m = 0          # inicializa a variável m com zero
n = 0          # inicializa a variável n com zero
for c in range(0, 5):  # para cada número de 0 a 4:
    # adiciona um valor digitado pelo usuário na lista
    listanum.append(int(input(f'Digite um valor para a posição {c} :')))
    # imprime a lista atualizada
    print(f'Os valores digitados foram: {listanum}')
    if c == 0:  # se for a primeira iteração do loop:
        # inicializa as variáveis m e men com o primeiro valor da lista
        m = men = listanum[c]
    else:  # caso contrário:
        if listanum[c] > m:  # se o valor atual for maior do que m:
            m = listanum[c]  # atualiza m com o valor atual
        if listanum[c] < n:  # se o valor atual for menor do que n:
            n = listanum[c]  # atualiza n com o valor atual

print('='*5, 'Prints', '='*5)  # imprime uma linha separadora
# imprime o maior número encontrado e prepara para imprimir as posições em que ele aparece
print(f'O maior número foi {m} nas posições: ', end='')
for i, v in enumerate(listanum):  # para cada índice e valor na lista:
    if v == m:  # se o valor for igual ao maior número encontrado:
        print(i)  # imprime o índice
# imprime o menor número encontrado e prepara para imprimir as posições em que ele aparece
print(f'O menor número foi {n} nas posições: ', end='')
for i, v in enumerate(listanum):  # para cada índice e valor na lista:
    if v == n:  # se o valor for igual ao menor número encontrado:
        print(i)  # imprime o índice

        #OUTRA FORMA SÓ QUE PARECIDA
listanum = []
n = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    print(f'Os valores digitados foram: {listanum}')
m = max(listanum)
n = min(listanum)
print('='*5, 'Prints', '='*5)
print(f'O maior número foi {m} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == m:
        print(i)
print(f'O menor número foi {n} nas posições: ', end='')
for i, v in enumerate(listanum):
    if v == n:
        print(i)
