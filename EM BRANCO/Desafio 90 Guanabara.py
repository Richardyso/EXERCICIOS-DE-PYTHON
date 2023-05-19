a = {}
n = str(input('Qual nome? '))
m = float(input('Qual a média? '))
a = {'nome': n, 'media': m}

if m >= 7:
    print(f'{a["nome"]} tem a média {a["media"]}, por isso está aprovado!')
else:
    print(f'{a["nome"]} tem a média {a["media"]}, por isso está reprovado!')
