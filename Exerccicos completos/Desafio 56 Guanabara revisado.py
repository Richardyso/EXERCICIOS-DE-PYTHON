idades = []
nomes = []
sexos = []
for c in range(0, 4):
    nome = input('Qual o nome? ')
    idade = int(input('Qual idade? '))
    idades.append(idade)
    sexo = input('Qual sexo? ')
    sexos.append(sexo)
    nomes.append(nome)

soma = sum(idades)
media = soma/4
maisvelho = 0
nomevelho = ''
for i in range(len(nomes)):
    if sexos[i] == 'm' and idades[i] > maisvelho:
        maisvelho = idades[i]
        nomevelho = nomes[i]

menores = 0
for idade in idades:
    if idade < 18:
        menores += 1
print(media)
print(nomevelho)
print('Existem :{} menores de idade femininas'.format(menores))
