import random
jogo = 0
jog1 = 0
print('JOGO DO PAR OU ÍMPAR')
comecar = str(input('Quer jogar?'))
while comecar == 's':
    aleatorio = random.randint(0, 100)
    parimpar = str(input('Vc quer par ou ímpar?'))
    n = int(input('Jogue um número aqui:'))

    final = aleatorio+n

    if final % 2 == 0 and parimpar == ('par'):
        print('Vc acertou, o número é par!')
        jogo = jogo+1
    elif final % 2 != 0 and parimpar == ('impar'):
        print('Vc acertou, o número é ímpar!')
        jogo = jogo+1
    else:
        print('VC ERROUUUUUU')
        jog1 = jog1+1
    continuar = str(input('Quer continuar no jogo?'))
    if continuar == 's':
        continue
    else:
        break

print(f'O total de partidas vencidas pelo computador, foi:{jog1}')
print(f'O total de partidas vencidas por você, foi:{jogo}')
print('Final do jogo!')
