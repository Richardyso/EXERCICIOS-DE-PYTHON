n1 = int(input('\033[31mEntre com o primeiro bimestre do aluno:\033[m'))
n2 = int(input('Entre com o segundo bimestre'))
n3 = int(input('Entre com o terceiro bimestre'))
n4 = int(input('Entre com o quarto bimestre'))
media = (n1 + n2 + n3 + n4) / 4
print('A média final do aluno é {}'.format(media))
if media >= 7.0:
    print('O aluno está aprovado!')
elif media >= 5 and media <= 6.9:
    print('O aluno esta de recuperação')
else:
    print('O aluno esta reprovado')
