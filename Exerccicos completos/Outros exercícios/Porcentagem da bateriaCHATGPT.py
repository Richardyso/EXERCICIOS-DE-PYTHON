valor = float(input("Qual a voltagem da bateria?"))
carregado = 4.2
descarregado = 3.2
if valor == carregado:
    valorfinal = 100
else:
    valorfinal = ((valor - descarregado) / (carregado - descarregado)) * 100

print(f"O nível da bateria é de {valorfinal}%")
