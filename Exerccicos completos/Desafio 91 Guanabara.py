from random import randint
n = []
j = {}
print('Os valores sorteados foram: ')
for c in range(1, 5):
    n.append(randint(0, 6))
j = {'jogador1': n[0], 'jogador2': n[1], 'jogador3': n[2], 'jogador4': n[3]}
print(j)
print('RANKING DOS JOGADORES')
posicao = sorted(n)
print(f'1º Lugar: ficou {posicao[3]}')
print(f'2º Lugar: ficou {posicao[2]}')
print(f'3º Lugar: ficou {posicao[1]}')
print(f'4º Lugar: ficou {posicao[0]}')

################# COMENTADO POR MIM MESMO######################
# from random import randint
# n = []
# j = {}
# print('Os valores sorteados foram: ')
# for c in range(1, 5):
#     n = (randint(0, 6))
#     p = (f'O jogador {c} tirou {n}')
#     j[f'jogador {c}'] = n
# # j = {'jogador1': n[0], 'jogador2': n[1], 'jogador3': n[2], 'jogador4': n[3]}       # OUTRA FORMA DE FAZER SÓ QUE FORA DO LAÇO
# # print(j[2][0])              # errado pois não é lista
# # print(j[2])                 # errado pois não é uma lista
# print(j['jogador 3'][0])      # errado pois não existe mais de um elemento em 'jogador 3'
# print(j['jogador 3'])         # correto
############# ABAIXO COM ERRO###########

# for x in n:
#     if x == max(n):
#         mm = x
#         print(f'1º Lugar: ficou {mm}')
#     if x == min(n):
#         nn = x
#         print(f'2º Lugar: ficou {nn}')
#     if x > min(n) and x < max(n):
#         a = x
#         print(f'3º Lugar: ficou {a}')
#     else:
#         print(f'4º Lugar: ficou {x}')


######################## SOLUÇÃO DO GPT########################
# from random import randint

# j = {f'jogador{c}': randint(0, 6) for c in range(1, 5)}

# print('Os valores sorteados foram:')
# print(j)

# print('RANKING DOS JOGADORES')
# posicao = sorted(j.values(), reverse=True)
# for i, valor in enumerate(posicao):
# print(f'{i+1}º Lugar: ficou {valor}')
