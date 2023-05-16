from random import randint
from time import sleep
print('-'*40)
print('MEGA SENA'.center(40))
print('-'*40)
q = int(input('Quantos jogos você quer que eu sorteie? '))
print('=*'*5, ' Sorteando os jogos ', '=*'*5)
for c in range(0, q):
    s = []
    for z in range(1, 7):
        s.append(randint(1, 60))
    print(f'Jogo {c+1}: {s}')
    sleep(1)
print('=*'*7, ' BOA SORTE ', '=*'*7)
