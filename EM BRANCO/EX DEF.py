# def tx():
#     print('=*'*30)


# # principal
# tx()
# print('Ola mundo')
# tx()
############################################# OU #######################################################

# def mensagem(tx):
#     print('=*'*30)
#     print(tx)
#     print('=*'*30)


# # principal
# mensagem('Olá mundo')
########################################################################################################


# Desempacotar
# def contador(*núm):
#     tam = len(núm)
#     print(f'Recebi os valores {núm} e são {tam} números')
#     print(' Fim')


# contador(1, 2, 3)
# contador(4, 5)
# contador(6, 7, 8, 9)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
