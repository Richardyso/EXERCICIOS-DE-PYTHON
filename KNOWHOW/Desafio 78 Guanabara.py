l = []
for c in range(0, 5):
    l.append(int(input(f'Digite um valor para a posição {c}: ')))

m = max(l)
n = min(l)
p1 = l.index(m)
p2 = l.index(n)
print(f'A lista ficou assim: {l}')
print(f'O maior valor foi {m} e foi encontrado na posição: {p1}')
print(f'O menor valor foi {n} e foi encontrado na posição: {p2}')


#MESMA COISA ABAIXO

# # Cria uma lista vazia chamada "numeros"
# numeros = []

# # Pede ao usuário que insira 5 valores numéricos e adiciona cada valor à lista "numeros"
# for i in range(5):
#     # Repete até que o usuário insira um valor numérico válido
#     while True:
#         try:
#             valor = int(input(f'Digite o {i+1}º valor: '))
#             break
#         except ValueError:
#             print('Valor inválido. Digite um número inteiro.')
    
#     numeros.append(valor)

# # Inicializa as variáveis "maior" e "menor" com o primeiro valor da lista "numeros"
# maior = menor = numeros[0]

# # Inicializa as variáveis "posicao_maior" e "posicao_menor" com 0
# posicao_maior = posicao_menor = 0

# # Percorre a lista "numeros" para encontrar o maior e o menor valor, e suas posições
# for i, numero in enumerate(numeros):
#     if numero > maior:
#         maior = numero
#         posicao_maior = i
#     elif numero < menor:
#         menor = numero
#         posicao_menor = i

# # Imprime a lista "numeros"
# print('A lista de números é:')
# for numero in numeros:
#     print(numero)

# # Imprime o maior valor e sua posição
# print(f'O maior valor é {maior} e foi encontrado na posição {posicao_maior}.')

# # Imprime o menor valor e sua posição
# print(f'O menor valor é {menor} e foi encontrado na posição {posicao_menor}.')




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
