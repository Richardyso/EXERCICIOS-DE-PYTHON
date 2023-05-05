maior = masculino = mulhermenor = 0

while True:
    i = int(input('Qual idade?'))
    s = str(input('Qual o sexo da pessoa?'))
    if i >= 18:
        maior = maior+1
    if s == 'm':
        masculino = masculino+1
    elif s == 'f' and i <= 20:
        mulhermenor = mulhermenor+1
    sn = str(input('Continuar adicionando dados?'))
    if sn == 's':
        continue
    else:
        break

print(f'O total de pessoas maiores de idade foi: {maior}')
print(f'O total de homens foi: {masculino}')
print(f'O total de mulheres menores de 20 anos foi: {mulhermenor}')
