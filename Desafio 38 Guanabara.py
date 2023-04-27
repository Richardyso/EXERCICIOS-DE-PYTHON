print('\033[31mSó pra lembrar a cor\033[m')
n1 = int(input('Entre o primeiro valor numérico:'))
n2 = int(input('Entre o segundo valor numérico:'))
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 == n2:
    print('Os valores são iguais')
else:
    print('O segundo valor é maior')
