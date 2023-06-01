def ficha(n='DESCONHECIDO', g=0):
    print(f'O jogador {n} fez {g} gols')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
