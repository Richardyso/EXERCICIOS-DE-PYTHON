ficha = []
while True:
    nome = str(input('Qual é o nome do aluno? '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    s = str(input('Quer adicionar mais alunos? ')).lower()
    if s != 's':
        break
print('=-'*20)
print('BOLETIM ESCOLAR'.center(40))
print('=-'*20)
print(f'Nº', 'NOME', 'MÉDIA')
for i, a in enumerate(ficha):
    print(f'{i} {a[0]} {a[2]}')
while True:
    opc = int(input('Mostrar as notas de qual aluno? '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

lc = [[], [[], []]]
while True:
    lc[0].append(str(input('Qual é o nome do aluno? ')))
    lc[1][0].append(float(input('1ª Nota: ')))
    lc[1][1].append(float(input('2ª Nota: ')))
    for i, aluno in enumerate(lc[0]):
        notas = [lc[1][0][i], lc[1][1][i]]  # VER[i]
        media = sum(notas) / 2
    s = input('Quer adicionar mais alunos? ').lower()
    print('=-'*20)
    print('BOLETIM ESCOLAR'.center(40))
    print('=-'*20)
    print(f'Nº', 'NOME'.center(30), 'MÉDIA')
    for x in lc[0]:
        print(len(lc[0]),     aluno,     media)

    if s != 's':
        break
    # for nota1, nota2 in enumerate(lc[0]):
    #     print(nota2)
    # m.append(soma)/2
    # for x in lc[0]:
    #     len(lc[0]), x.center(33), m


# p = int(input('Quer revisar as notas de qual aluno? ')).lower()
    # if p == 'n':
    #     break

# # print('Boletim')
# # print(int(input('De qual aluno deseja ver as notas? (999 interrompe)')))
