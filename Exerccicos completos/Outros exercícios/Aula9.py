import re
# frase= 'curso em video'
texto='''Hoje é um dia ensolarado, com um céu azul tão profundo que parece uma pintura. Caminho pelas ruas movimentadas da cidade, onde as pessoas passam apressadas, indo e vindo de seus compromissos. Observo as vitrines das lojas, cheias de produtos tentadores e promessas de felicidade. À minha frente, uma placa de sinalização indica que ainda faltam 2 quilômetros para chegar ao meu destino. Respiro fundo, aperto o passo e digito o endereço no GPS do meu celular. Ao som dos carros e buzinas, continuo minha jornada, determinado a chegar onde preciso antes das 14h.'''
textoo= (texto.capitalize().count('c'))
quanto=len(texto)
print(quanto)
print(textoo)
print(texto.replace('céu','aksjdisudhiasud'))
existe='ela'in texto
print(existe)
print(texto.count('eu'))
dividido=texto.split()
quantos= texto.count(dividido)
print(dividido)
# print(texto)