print('TRÊM BÃO, SÔ')
n = ((int(input('Digite aqui um valor: '))),
     (int(input('Digite outro valor: '))),
     (int(input('Digite mais um valor: '))),
     (int(input('Digite o último valor: '))),)
print(f'Você digitou os valores: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro numero 3 apareceu na posição {n.index(3)+1}')
else:
    print(f'O valor 3 não foi digitado!')
print(f'Os valores pares digitados foram: ', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
