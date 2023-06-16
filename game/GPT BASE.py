import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 203
altura = 252
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olavo')

cores = (0, 0, 255)  # Cor dos retângulos

retangulos = [
    (0, 0, 50, 50),     # Quadrados
    (51, 0, 50, 50),
    (102, 0, 50, 50),
    (153, 0, 50, 50),
    (0, 51, 50, 100),   # Retângulo em pé
    (51, 51, 50, 100),
    (102, 51, 50, 100),
    (153, 51, 50, 100),
    (0, 152, 100, 50),  # Retângulo deitado
    (102, 152, 100, 100)  # Quadradão
]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    for retangulo in retangulos:
        pygame.draw.rect(tela, cores, retangulo)

    pygame.display.update()
