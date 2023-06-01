import tkinter as tk
from tkinter import messagebox
import pygame

# Inicialização do Pygame
pygame.init()

# Dimensões da janela do jogo da velha
WIDTH, HEIGHT = 300, 300
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicialização da janela do jogo da velha usando Tkinter
root = tk.Tk()
root.title("Jogo da Velha")

# Criação da tela do jogo da velha usando Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

# Variáveis de controle do jogo
board = [['' for _ in range(COLS)] for _ in range(ROWS)]
current_player = 'X'
game_over = False

# Função para desenhar o tabuleiro do jogo da velha


def draw_board():
    screen.fill(WHITE)

    # Desenhar linhas horizontais
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE), (WIDTH, CELL_SIZE))
    pygame.draw.line(screen, BLACK, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE))

    # Desenhar linhas verticais
    pygame.draw.line(screen, BLACK, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT))
    pygame.draw.line(screen, BLACK, (2 * CELL_SIZE, 0),
                     (2 * CELL_SIZE, HEIGHT))

    # Desenhar símbolos (X ou O) nas células ocupadas
    for row in range(ROWS):
        for col in range(COLS):
            symbol = board[row][col]
            if symbol != '':
                font = pygame.font.Font(None, 100)
                text = font.render(symbol, True, BLACK)
                text_rect = text.get_rect(
                    center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

# Função para verificar se houve vitória


def check_win():
    # Verificar linhas
    for row in range(ROWS):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True

    # Verificar colunas
    for col in range(COLS):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True

    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False

# Função para verificar se o tabuleiro está cheio (empate)


def check_draw():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == '':
                return False
    return True

# Função para reiniciar o jogo


def restart_game():
    global board, current_player, game_over
    board = [['' for _ in range(COLS)] for _ in range(ROWS)]
