c = 's'
final = []
n = 0

while c != 'n':
    n = int(input('Digite um valor: '))
    c = str(input('Quer continuar digitando novos valores? '))
    final.append(n)
    p = max(final)
    m = min(final)

media = sum(final) / len(final)

print('A média entre os valor digitados foi: {}!'.format(media))
print('O maior número lido foi: {}!'.format(p))
print('O menor número lido foi: {}!'.format(m))
