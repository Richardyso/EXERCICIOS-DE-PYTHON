import math
nome1 = str(input('Qual o primeiro nome? '))
idade1 = int(input('Qual a primeira idade? '))
s1 = str(input('Qual o sexo da pessoa?'))

nome2 = str(input('Qual o segundo nome? '))
idade2 = int(input('Qual a segunda idade? '))
s2 = str(input('Qual o sexo da pessoa?'))

nome3 = str(input('Qual o terceiro nome? '))
idade3 = int(input('Qual a terceira idade? '))
s3 = str(input('Qual o sexo da pessoa?'))

nome4 = str(input('Qual o quarto nome? '))
idade4 = int(input('Qual a quarta idade? '))
s4 = str(input('Qual o sexo da pessoa?'))

listanome = [nome1, nome2, nome3, nome4]
listaidade = [idade1, idade2, idade3, idade4]
sexo = [s1, s2, s3, s4]
media = sum(listaidade) / len(listaidade)

homemvelho = 0
idadehomem = -math.inf
for c in range(len(listaidade)):
    if sexo[c] == 'M' and listaidade[c] > idadehomem:
        homemvelho = listanome[c]
        idadehomem = listaidade[c]

mulher20 = 0
for b in range(len(listaidade)):
    if sexo[b] == 'F' and listaidade[b] < 20:
        mulher20 += 1

print('A idade média das pessoas é: {} anos'.format(media))
print('O homem mais velho é o {}'.format(homemvelho))
print('A quantidade de mulheres abaixo de 20 anos é: {}'.format(mulher20))
