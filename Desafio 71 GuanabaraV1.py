print('CAIXA ELETRÔNICO')
r = int(input('Digite aqui o valor que você deseja sacar!'))
s = list(str(r))
# m, c, d, u = s
m = s[0]
c = s[1]
d = s[2]
u = s[3]
milhar = int(m)*1000
centena = int(c)*100
dezena = int(d)*10
unidade = int(u)
milha = 50
cen = 20
dez = 10
u = 1

d50m = milhar/milha
d20c = centena/cen
d10d = dezena/dez
d1u = unidade+0
print(f'Você receberá {d50m: .0f} cédulas de {milha} reais, {d20c: .0f} cédulas de {cen} reais,{d10d: .0f} cédulas de {dez} reais e {d1u} cédulas de {u} real')
print(f'Totalizando {d50m+d20c+d10d+d1u:.0f} cédulas!')
print('-VOLTE SEMPRE-')
