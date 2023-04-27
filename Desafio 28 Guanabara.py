import random
print('Primeiro jogo')
n1 = random.randint(0, 5)
n = int(input('Chute o valor escolhido pelo computador:'))
if n == n1:
    print('Acertou!!')
else:
    print('Errou')
