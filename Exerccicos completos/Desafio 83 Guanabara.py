b = str(input('Entre com uma expressão matemática: '))
s = b.count('(') + b.count(')')
if s % 2 == 0:
    print('A expressão está correta!')
else:
    print('A expressão matemática digitada está incorreta!!')
