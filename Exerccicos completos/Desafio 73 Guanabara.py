print('CAMPEONATO BRASILEIRO DE FUTEBOL')
time = ('Flamengo', 'Vasco', 'Grêmio', 'Fluminese', 'Botafogo', 'Esporte', 'São Paulo', 'Palmeiras',
        'Corinthians', 'Milão', 'Real Madri', 'Barcelona', 'Bocajuniors', 'Atlético Mineiro', 'Santos', 'Internacional', 'Cruzeiro', 'Chapecoense', 'Santa Cruz', 'Criciúma')
for ss in (time):
    ss = time[17]
rebaixado = (time[-4:])
primeiros = (time[0:5])
ordem = (sorted(time))
print(f'O Top 5 times foram: {primeiros}')
print(f'Os 4 times rebaixados foram: {rebaixado}')
print(f'Os times em ordem alfabética ficam assim:{ordem}')
print(f'O time {ss} está na posição: {17}!')
