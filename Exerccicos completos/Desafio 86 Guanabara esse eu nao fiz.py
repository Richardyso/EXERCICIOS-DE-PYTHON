m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor: [{l}, {c}]'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]}]', end='')
    print()


# # # # METODO GPT
# m = [[], [], []]
# for i in range(0, 3):  # loop para ler os valores das linhas
#     for j in range(0, 3):  # loop para ler os valores das colunas
#         # leitura do valor e armazenamento na variável v
#         v = int(input(f'Digite um valor para [{i}, {j}]: '))
#         m[i].append(v)  # adiciona o valor lido na lista da linha i
# print(m)  # exibe a matriz completa
