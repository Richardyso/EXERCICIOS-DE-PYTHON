################################################ DEF BASICO
# def linha():
#     print('=='*15)


# #PRINCIPAL
# linha()
# print('SISTEMA DE ALUNO'.center(30))
# linha()
# print('CADASTRO DE FUNCIONÁRIOS'.center(30))
# linha()
# print('ERROS DO SISTEMA'.center(30))
# linha()
################################################ DEF PARÂMETROS DEFINIDOS
# def mensagem(msg):
#     print('=='*15)
#     print(msg.center(30))
#     print('=='*15)


# mensagem('SISTEMA DE ALUNO')
# mensagem('CADASTRO DE FUNCIONÁRIOS')
# mensagem('ERROS DO SISTEMA')
################################################ DEF COM VALORES
# def soma(a,b,c=0):
#     d=a+b+c
#     print(d)


# soma(b=4,a=2)
# soma(9,2)
################################################ Empacotar
# def contador(* núm):
#     tam = len(núm)
#     print(f'Recebi os valores {núm} e são {tam} números')
#     print(' Fim')


# contador(1, 2, 3)
# contador(4, 5)
# contador(6, 7, 8, 9)
#####################################################################
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
