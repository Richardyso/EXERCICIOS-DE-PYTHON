a = int (input('Primeiro valor:'))
b = int (input("Segundo valor:"))
c = int (input("Terceiro valor:"))
if a > b and a > c:
    print('O maior numero é:{}' .format(a))
if b > a and b > c:
    print('O maior numero é:{}' . format(b))
if c > a and c > b:
    print('O maior numero é:{}' . format(c))
if a == b == c: print ('Os valores são iguais')
#
# if a > b and a > c:
#     print('O maior numero é {}' . format(a))
# elif b > a and b > c:
#     print('O maior numero é {}' . format(b))
# else:
#     print('O maior numero é {}' . format(c))