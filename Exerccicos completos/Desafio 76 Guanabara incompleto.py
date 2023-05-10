lista = ('Pão', 1, 'Cuscuz', 3.9, 'Suco', 6.5, 'Kitut',
         10, 'Fone de Ouvido', 100, 'Perfume', 200)
print(40 * '-')
texto1 = 'Os ítens organizados ficaram assim:'
centralizado = texto1.center(40)
print(centralizado)
print(40 * '-')
tcampo = 40
cpreenchimento = '.'
texto = '.'
# camp = '.'*30
# campo = camp.center(10)
campo = texto.rjust(tcampo, cpreenchimento)
print(lista[0], campo, 'R$ ', lista[1])
print(lista[2], campo, 'R$ ', lista[3])
print(lista[4], campo, 'R$ ', lista[5])
print(lista[6], campo, 'R$ ', lista[7])
print(lista[8], campo, 'R$ ', lista[9])
print(lista[10], campo, 'R$ ', lista[11])
print(40 * '-')
