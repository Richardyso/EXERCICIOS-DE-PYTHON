from random import randint
from time import sleep
numeros = []


def sorteia(lista):
    print('Sorteando 5 valores...')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('Pronto')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares foi {soma}')


# PROGRAMA
sorteia(numeros)
somapar(numeros)
