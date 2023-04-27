print('\033[44mTESTADOR CREDPAGO\033[m')
nome = str(input('Qual seu nome: '))
salario = int(input('Qual sua renda mensal, {}?'.format(nome)))
valorcasa = int(input('Qual o valor do imóvel?'))
parcela = int(input('Deseja parcelar em quantas vezes, {}?'.format(nome)))
parcela1 = valorcasa/parcela

if parcela1 >= salario*(salario*100/30):
    print('\033[31;107mO empréstimo para comprar o imóvel não foi aprovado!!\033[m')
else:
    print('Seu empréstimo está aprovado!/n Sua parcela será de:R$ {} por mês!'.format(parcela1))
