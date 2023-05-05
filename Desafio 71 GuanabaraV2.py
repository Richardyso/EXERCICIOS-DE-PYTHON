r = int(input('Digite aqui o valor que você deseja sacar!'))
notas = [50, 20, 10, 1]

d50 = r//notas[0]
resto1 = r % notas[0]

d20 = resto1//notas[1]
resto2 = resto1 % notas[1]

d10 = resto2//notas[2]
resto3 = resto2 % notas[1]

d1 = resto3//notas[3]
resto3 = resto3 % notas[3]

print(
    f'Você receberá {d50:.0f} cédulas de {notas[0]} reais, {d20:.0f} cédulas de {notas[1]} reais,{d10:.0f} cédulas de {notas[2]} reais e {d1:.0f} cédulas de {notas[3]} real')
print(f'Totalizando {d50+d20+d10+d1:.0f} cédulas!')
print('-VOLTE SEMPRE-')
