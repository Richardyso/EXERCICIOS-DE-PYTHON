from time import sleep


def linha():
    print('=*'*20)


def fim():
    print('Fim')


linha()
contagem1 = 1
print('Contagem de 1 até 10 de 1 em 1:')
for c in range(10):
    print(f'{contagem1}', end=' ', flush=True)
    contagem1 += 1
    sleep(1)
fim()
linha()
contagem10 = 10
print('Contagem de 10 até 0 de 2 em 2')
for z in range(5):
    print(contagem10, flush=True)
    contagem10 = contagem10-2
    sleep(1)
fim()
linha()
