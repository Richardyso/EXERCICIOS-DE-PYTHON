palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'video', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'inteligencia')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in vogais:
            print(letra, end=' ')
    # vogais = ('a', 'e', 'i', 'o', 'u')
    # if vogais[0] in palavras[0]:
    #     l0 = vogais[0].upper()
    # else:
    #     l0 = ' '
    # if vogais[1] in palavras[0]:
    #     l1 = vogais[1].upper()
    # else:
    #     l1 = ' '
    # if vogais[2] in palavras[0]:
    #     l2 = vogais[2].upper()
    # else:
    #     l2 = ' '
    # if vogais[3] in palavras[0]:
    #     l3 = vogais[3].upper()
    # else:
    #     l3 = ' '
    # if vogais[4] in palavras[0]:
    #     l4 = vogais[4].upper()
    # else:
    #     l4 = ' '
    # # vall=(l0+l1+l2+l3+l4)

    # print(f'Na palavra {palavras[0].upper()} temos: {(l0+l1+l2+l3+l4)}')

    # # # ocorrencias = palavras[1].count(vogais[2])
    # # # print(ocorrencias)
