palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'video', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'inteligencia')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'\nNa palavra: {p}, temos: ', end='')
    for letra in p:
        if letra in vogais:
            print(letra, end='')
