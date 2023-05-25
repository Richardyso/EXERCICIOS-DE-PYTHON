from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1
    if p == 0:
        p == 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont = cont+p
            sleep(1)
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont = cont-p
            sleep(1)
        print('Fim')


# Principal
contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Qual o início você quer? '))
final = int(input('Qual o valor final? '))
passo = int(input('Qual o passo você quer? '))

if final > inicio:
    for a in range(inicio, final + 1, passo):
        print(a, end=' ', flush=True)
        sleep(1)
else:
    for a in range(inicio, final - 1, -passo):
        print(a, end=' ', flush=True)
        sleep(1)
print('Fim')
