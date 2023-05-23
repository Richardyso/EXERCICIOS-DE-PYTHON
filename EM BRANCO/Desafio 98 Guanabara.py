from time import sleep


def linha():
    print('=*'*20)


def fim():
    print('Fim')


linha()
passo1 = 1
print('Contagem de 1 até 10 de 1 em 1:')
for c in range(10):
    print(f'{passo1}', end=' ', flush=True)
    passo1 += 1
    sleep(1)


fim()
linha()
passo10 = 10
print('Contagem de 10 até 0 de 2 em 2')
for z in range(5):
    print(passo10, end=' ', flush=True)
    passo10 = passo10-2
    sleep(1)
fim()
linha()

inicio = int(input('Qual o inicio você quer? '))
final = int(input('Qual o valor final? '))
passo = int(input('Qual o passo você quer? '))
for a in range(inicio, final) or range(final, inicio):
    if final > inicio:
        print(inicio, end=' ', flush=True)
        inicio = inicio+passo
        sleep(1)
    if final < inicio:  # nao funciona
        print(inicio, end=' ', flush=True)
        inicio = inicio-passo
        sleep(1)
