import random
print('\033[4;31;40mJOGO DA ADIVINHAÇÃO\033[m')
n = 0
r = random.randint(0, 10)
tentativas = 0
while n != r:
    print('Você errou o número!!!')
    n = int(input('Chute um valor entre 1 e 10: '))
    tentativas += 1
print('Você acertou!!!')
print('Você fez {} tentativas'.format(tentativas))
