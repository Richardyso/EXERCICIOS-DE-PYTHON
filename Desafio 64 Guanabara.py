n1 = 0
digitados = []
quantos = 0
print('Desafio 64 do Guanabara')
while n1 != 999:
    n1 = int(input('Digite um número inteiro: '))
    if n1 != 999:
        digitados.append(n1)
        quantos = quantos+1
soma = sum(digitados)
print('OS números digitados foram: {} !'.format(quantos))
print('A soma dos números digitados foi {} !'.format(soma))
print('Final do Programa!!!')
