t = ('Pão', 1, 'Cuscuz', 3.9, 'Suco', 6.5,
     'Kitut', 10, 'Fone de ouvido', 100, 'Perfume', 200)
print(f'Nome: {t[0].ljust(15)} Preço: {str(t[1]).ljust(3)}R$')
print(f'Nome: {t[2].ljust(15)} Preço: {str(t[3]).ljust(3)}R$')
print(f'Nome: {t[4].ljust(15)} Preço: {str(t[5]).ljust(3)}R$')
print(f'Nome: {t[6].ljust(15)} Preço: {str(t[7]).ljust(3)}R$')
print(f'Nome: {t[8].ljust(15)} Preço: {str(t[9]).ljust(3)}R$')
print(f'Nome: {t[10].ljust(15)} Preço: {str(t[11]).ljust(3)}R$')
# OUUUUUUUUUUUUUUUUUU
a = [0, 2, 4, 6, 8, 10]
b = [1, 3, 5, 7, 9, 11]
n = ([t[i] for i in a])
P = ([t[o] for o in b])
print(f'Nome: {n[0].ljust(15)} Preço: {str(P[0]).ljust(3)}R$')
print(f'Nome: {n[1].ljust(15)} Preço: {str(P[1]).ljust(3)}R$')
print(f'Nome: {n[2].ljust(15)} Preço: {str(P[2]).ljust(3)}R$')
print(f'Nome: {n[3].ljust(15)} Preço: {str(P[3]).ljust(3)}R$')
print(f'Nome: {n[4].ljust(15)} Preço: {str(P[4]).ljust(3)}R$')
print(f'Nome: {n[5].ljust(15)} Preço: {str(P[5]).ljust(3)}R$')
