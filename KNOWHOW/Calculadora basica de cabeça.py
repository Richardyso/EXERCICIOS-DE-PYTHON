print('-='*15)
print('Minha primeira calculadora'.center(30))
print('-='*15)
v1 = int(input('Insira um valor inteiro: '))
v2 = int(input('Insira outro valor inteiro: '))
a = (str(input('Deseja fazer qual operação aritmética? [+ - * /]')))
if a == '+':
    r = v1+v2
if a == '-':
    if v1 > v2:
        r = v1-v2
    else:
        r = v2-v1
if a == '*':
    r = v1*v2
if a == '/':
    r = v1/v2
print(f'Resposta: {r}')
