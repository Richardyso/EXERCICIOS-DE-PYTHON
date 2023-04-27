distancia = int(input('Qual a distância da viagem:'))
if distancia <= 200:
    valor1 = (distancia*0.5)+distancia
    print('O valor da viagem será:{} reais'.format(valor1))
else:
    valor2 = (distancia*0.45)+distancia
    print('O valor da viagem será:{} reais'.format(valor2))
