p1 = int(input('Digite valor:'))
p2 = int(input('Digite o valor:'))
p3 = int(input('Digite outro valor:'))
p4 = int(input('Digite ultimo:'))
valores = [p1, p2, p3, p4]
maxi = max(valores)
if p1 > maxi:
    print('O {} Foi o maior valor'.format(p1))
elif p2 > maxi:
    print('O {} Foi o maior valor'.format(p2))
elif p3 > maxi:
    print('O {} Foi o maior valor'.format(p3))
else:
    print('O {} Foi o maior valor'.format(p4))
