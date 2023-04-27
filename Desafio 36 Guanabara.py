print('\033[44mTESTADOR CREDPAGO\033[m')
nome = str(input('Qual seu nome: '))
salario = int(input('Qual sua renda mensal, {}?'.format(nome)))
valorcasa = int(input('Qual o valor do imóvel?'))
parcelas = int(input('Deseja parcelar em quantas vezes, {}?'.format(nome)))
parceladoimovel = valorcasa/parcelas
posso = salario*0.3
if posso <= valorcasa*0.3:
    print('\033[31;107mO empréstimo para comprar o imóvel não foi aprovado!!\033[m')
else:
    print('Seu empréstimo está aprovado, sua parcela será de:R$ {:.2f} por mês!'.format(
        parceladoimovel))
