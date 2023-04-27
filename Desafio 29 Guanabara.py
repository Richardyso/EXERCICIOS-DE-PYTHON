# Entre com a velocidade de um carro, se ele ultrapassar 80KM receberá uma multa de 7R$ por cada KM que passar do limite
print('Multrômetro manual:')
velocidade = int(input('Qual a velocidade do carro?'))
if velocidade >= 80:
    multa = (velocidade-80)
    print('O valor da multa será de: {}R$'.format(multa))
else:
    print('Não tomou multa')
