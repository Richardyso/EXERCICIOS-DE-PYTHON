print('NOVA TAUBUADA!')
n = int(input('Qual número você quer saber a tabuada?'))
if n >= 0:
    for c in range(1, 11):
        resultado = n*c
        n1 = print(f'O valor de {n} X {c} = {resultado}')
else:
    print('Favor digitar um número positivo!')
