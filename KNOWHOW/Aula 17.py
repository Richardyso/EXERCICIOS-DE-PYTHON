grupo = []
dado = []
for c in range(3):
    dado.append(str(input('Digite nome: ')))
    dado.append(int(input('Digite a idade: ')))
    grupo.append(dado[:])
    dado.clear()
print(len(grupo))
#
