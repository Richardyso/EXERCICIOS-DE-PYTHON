n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
while True:
    print('Digite 1 para somar!')
    print('Digite 2 para multiplicar!')
    print('Digite 3 para o maior numero.')
    print('Digite 4 para novos números.')
    print('Digite 5 para sair do Programa')
    opcao = int(input('Digite aqui: '))
    if opcao == 1:
        s = n1+n2
        print('\033[4;31;40mA soma de {} com {}, da: {} \033[m'.format(n1, n2, s))
    elif opcao == 2:
        m = n1*n2
        print(
            '\033[4;31;40mA multiplicação de {} com {}, da: {} \033[m'.format(n1, n2, m))
    elif opcao == 3:
        if n1 > n2:
            print('\033[4;31;40mO maior valor foi {}:\033[m'.format(n1))
        else:
            print('\033[4;31;40mO maior valor foi {}:\033[m'.format(n2))
    elif opcao == 4:
        n1 = int(
            input('\033[4;31;40mInsira novamente o primeiro número: \033[m'))
        n2 = int(
            input('\033[4;31;40mInsira novamente o segundo número: \033[m'))
    elif opcao not in [1, 2, 3, 4, 5]:
        print('\033[4;31;40mOpção inválida. Tente novamente.\033[m')

    elif opcao == 5:
        break


print('\033[4;31;40mADEUS!!!\033[m')
