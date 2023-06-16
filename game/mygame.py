import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 203
altura = 252
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olavo')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
# QUADRADOS 50X50
    pygame.draw.rect(tela, (0, 0, 255), (0, 0, 50, 50))
    pygame.draw.rect(tela, (0, 0, 255), (51, 0, 50, 50))
    pygame.draw.rect(tela, (0, 0, 255), (102, 0, 50, 50))
    pygame.draw.rect(tela, (0, 0, 255), (153, 0, 50, 50))
#  RETANGULO EM PÉ
    pygame.draw.rect(tela, (0, 0, 255), (0, 51, 50, 100))
    pygame.draw.rect(tela, (0, 0, 255), (51, 51, 50, 100))
    pygame.draw.rect(tela, (0, 0, 255), (102, 51, 50, 100))
    pygame.draw.rect(tela, (0, 0, 255), (153, 51, 50, 100))
# RETANGULO DEITADO
    pygame.draw.rect(tela, (0, 0, 255), (0, 152, 100, 50))
# QUADRADAO
    pygame.draw.rect(tela, (0, 255, 255), (102, 152, 100, 100))
    pygame.display.update()
############################################################################
# 5x4
# 5 linhas/altura
# 4 colunas/largura

# largura = 200
# altura = 200

# quadrado
# (50,50)

# retangulo deitado
# (100,50)

# retangulo em pé
# (50,100)
