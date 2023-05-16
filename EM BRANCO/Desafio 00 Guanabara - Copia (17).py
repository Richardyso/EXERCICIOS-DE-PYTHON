lc = [[], [[], []]]
while True:
    lc[0].append(str(input('Qual é o nome do aluno? ')))
    lc[1][0].append(int(input('1ª Nota: ')))
    lc[1][1].append(int(input('2ª Nota: ')))
    s = input('Quer adicionar mais alunos? ').lower()
    if s != 'sim':
        break
for i, aluno in enumerate(lc[0]):
    notas = [lc[1][0][i], lc[1][1][i]]  # VER[i]
    media = sum(notas) / 2
    # for nota1, nota2 in enumerate(lc[0]):
    #     print(nota2)
    # m.append(soma)/2
    # for x in lc[0]:
    #     len(lc[0]), x.center(33), m

print('=-'*20)
print('BOLETIM ESCOLAR'.center(40))
print('=-'*20)
print(f'Nº', 'NOME'.center(30), 'MÉDIA')
for x in lc[0]:
    print(len(lc[0]),     aluno,     media)

# p = int(input('Quer revisar as notas de qual aluno? ')).lower()
    # if p == 'n':
    #     break

# # print('Boletim')
# # print(int(input('De qual aluno deseja ver as notas? (999 interrompe)')))
