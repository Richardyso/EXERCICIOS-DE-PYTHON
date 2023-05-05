ano = int(input('Qual ano a criança nasceu:'))
idade = 2023-ano
if idade <= 9:
    print('Equipe Mirim')
elif idade >= 14 and idade <= 17:
    print('Infantil')
elif idade >= 19 and idade <= 20:
    print('Sênior')
elif idade > 20:
    print('Master')
