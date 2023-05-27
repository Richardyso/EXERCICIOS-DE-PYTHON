lista = []
while True:
    nome = str(input('Qual é o nome do aluno? '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media])
    r = str(input('Quer adicionar mais? '))
    if r == 'n':
        break
for i, a in enumerate(lista):
    print('Nº', 'NOME', 'MÉDIA')
    print(i, a[0], a[2])
while True:
    m = int(input('Mostrar as notas de qual aluno? '))
    if m <= len(lista)-1:
        print(f'Notas de {lista[m][0]} são {lista[m][1]}')
    if m == 999:
        break
