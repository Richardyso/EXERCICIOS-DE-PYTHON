texto = input("Digite um texto: ")
contador = 0

for letra in texto:
    if letra == 's' or letra == 'S':
        contador += 1

print("O texto tem {} letra(s) 's'.".format(contador))
