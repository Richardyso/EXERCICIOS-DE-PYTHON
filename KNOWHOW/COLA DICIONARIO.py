pessoas = {'nome': 'gustavo', 'sexo': 'm', 'idade': 22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# del pessoas['sexo']             #DELETAR
print(pessoas.items())  # printa tudao organizado por [lista] e (tupla)
print(pessoas)  # printa tudao como dicionario msm com {} apenas
pessoas['nome'] = 'Leandro'     # modificando
pessoas['peso'] = 99            # adicionando

for k, v in pessoas.items():    # for timo enumerate
    print(f'{k}={v}')

# for k in pessoas.values():    #for tipo simples
#     print(k)

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])

brasil = []  # lista
estado = {}  # dicionario
for c in range(3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Qual a sigla: '))
    brasil.append(estado.copy())  # não pode fatiar estado[:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {e}.')
