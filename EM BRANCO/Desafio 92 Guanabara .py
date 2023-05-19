# #primeiro feito só pra organizar#####################
# considerando ano de entrada sem sair da empresa e 35 anos de colaboração
while True:
    n = str(input('Qual o nome da pessoa? ')).capitalize()
    nasc = int(input('Qual ano de nascimento? '))
    ct = int(input('Qual número da carteira de trabalho? [0 para nao tem]'))
    if ct == 0:
        idade = 2023-nasc
        print(f'O nome é: {n}, e tem {idade} anos.')
        break
    ano = int(input('Qual foi o ano de contratação desse funcionário? '))
    s = input('Qual o valor do salário bruto da pessoa? ')
    print('-='*50)
    trab = 2023-ano
    apos = (ano+35)-nasc
    idade = 2023-nasc
    print(
        f'O nome é: {n}, e tem {idade} anos, trabalha a {trab} anos na empresa, vai se aposentar com {apos} anos e receberá {s}R$ de aposentadoria.')
    break


##############################################SEGUNDO FEITO ADICIONA APENAS PERGUNTA FINAL
# while True:
#     n = str(input('Qual o nome da pessoa? ')).capitalize()
#     nasc = int(input('Qual ano de nascimento? '))
#     ct = int(input('Qual número da carteira de trabalho? [0 para nao tem]'))
#     if ct == 0:
#         idade = 2023-nasc
#         print(f'O nome é: {n}, e tem {idade} anos.')
#         break
#     ano = int(input('Qual foi o ano de contratação desse funcionário? '))
#     s = input('Qual o valor do salário bruto da pessoa? ')
#     print('-='*50)
#     trab = 2023-ano
#     apos = (ano+35)-nasc
# idade = 2023-nasc
#     print1 = (
#         f'O nome é: {d["nome"]}, tem {d["idade"]} anos, trabalha a {d["anoemp"]} anos na empresa, vai se aposentar com {d["idadeap"]} anos e receberá {d["salario"]}R$ de aposentadoria.')
#     mais = str(input('Adicionar mais funcionários?')).lower()
#     if mais == 'n':
#         print(print1)
#         break



####################solução mais completa do gpt########################
####################solução mais completa do gpt########################
####################solução mais completa do gpt########################

# funcionarios = []

# while True:
#     d = {}
#     n = str(input('Qual o nome da pessoa? ')).capitalize()
#     nasc = int(input('Qual ano de nascimento? '))
#     ct = int(input('Qual número da carteira de trabalho? [0 para não tem]'))
    
#     if ct == 0:
#         idade = 2023 - nasc
#         print(f'O nome é: {n}, e tem {idade} anos.')
#         break
    
#     ano = int(input('Qual foi o ano de contratação desse funcionário? '))
#     s = input('Qual o valor do salário bruto da pessoa? ')
#     print('-=' * 50)
    
#     trab = 2023 - ano
#     apos = (ano + 35) - nasc
#     idade = 2023 - nasc
    
#     d = {'nome': n, 'idade': idade, 'anoemp': trab, 'idadeap': apos, 'salario': s}
#     funcionarios.append(d)
    
#     print1 = (
#         "O nome é: {nome}, tem {idade} anos, trabalha há {anoemp} anos na empresa, "
#         "vai se aposentar com {idadeap} anos e receberá {salario}R$ de aposentadoria."
#     )
    
#     mais = str(input('Adicionar mais funcionários?')).lower()
    
#     if mais == 'n':
#         break

# print('RANKING DOS FUNCIONÁRIOS')
# for funcionario in funcionarios:
#     print(print1.format(**funcionario))
#     print('-' * 50)

