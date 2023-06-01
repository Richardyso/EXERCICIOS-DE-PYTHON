

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual-ano
    if idade < 16:
        return f'Com {idade} anos não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos voto opcional'
    else:
        return f'Com {idade} anos o voto é obrigatório'


print('='*30)
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
