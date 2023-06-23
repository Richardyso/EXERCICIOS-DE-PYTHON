import pygame

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configurações da janela
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Movendo Objetos")

# Posição inicial dos objetos
square_pos = [(100, 100), (200, 200), (300, 300)]
retangulos_pos = [(400, 100), (500, 200), (600, 300)]
horizontal_rect_pos = (400, 400)
square_size = 50
retangulo_width = 80
retangulo_height = 40
horizontal_rect_width = 120
horizontal_rect_height = 60

# Objeto selecionado para movimento
selected_object = None


def handle_events():
    global selected_object

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            selected_object = None
            for i, pos in enumerate(square_pos):
                if pygame.Rect(pos[0], pos[1], square_size, square_size).collidepoint(mouse_pos):
                    selected_object = ("square", i)
            if pygame.Rect(horizontal_rect_pos[0], horizontal_rect_pos[1], horizontal_rect_width, horizontal_rect_height).collidepoint(mouse_pos):
                selected_object = ("horizontal_rect", None)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()


def move_left():
    global selected_object

    if selected_object[0] == "square":
        i = selected_object[1]
        x, y = square_pos[i]
        x -= square_size
        if not check_collision((x, y, square_size, square_size), retangulos_pos) and not check_collision(
                (x, y, square_size, square_size), horizontal_rect_pos):
            square_pos[i] = (x, y)
    elif selected_object[0] == "horizontal_rect":
        x, y = horizontal_rect_pos
        x -= square_size
        if not check_collision((x, y, horizontal_rect_width, horizontal_rect_height), square_pos) and not check_collision(
                (x, y, horizontal_rect_width, horizontal_rect_height), retangulos_pos):
            horizontal_rect_pos = (x, y)


def move_right():
    global selected_object

    if selected_object[0] == "square":
        i = selected_object[1]
        x, y = square_pos[i]
        x += square_size
        if not check_collision((x, y, square_size, square_size), retangulos_pos) and not check_collision(
                (x, y, square_size, square_size), horizontal_rect_pos):
            square_pos[i] = (x, y)
    elif selected_object[0] == "horizontal_rect":
        x, y = horizontal_rect_pos
        x += square_size
        if not check_collision((x, y, horizontal_rect_width, horizontal_rect_height), square_pos) and not check_collision(
                (x, y, horizontal_rect_width, horizontal_rect_height), retangulos_pos):
            horizontal_rect_pos = (x, y)


def move_up():
    global selected_object

    if selected_object[0] == "square":
        i = selected_object[1]
        x, y = square_pos[i]
        y -= square_size
        if not check_collision((x, y, square_size, square_size), retangulos_pos) and not check_collision(
                (x, y, square_size, square_size), horizontal_rect_pos):
            square_pos[i] = (x, y)
    elif selected_object[0] == "horizontal_rect":
        x, y = horizontal_rect_pos
        y -= square_size
        if not check_collision((x, y, horizontal_rect_width, horizontal_rect_height), square_pos) and not check_collision(
                (x, y, horizontal_rect_width, horizontal_rect_height), retangulos_pos):
            horizontal_rect_pos = (x, y)


def move_down():
    global selected_object

    if selected_object[0] == "square":
        i = selected_object[1]
        x, y = square_pos[i]
        y += square_size
        if not check_collision((x, y, square_size, square_size), retangulos_pos) and not check_collision(
                (x, y, square_size, square_size), horizontal_rect_pos):
            square_pos[i] = (x, y)
    elif selected_object[0] == "horizontal_rect":
        x, y = horizontal_rect_pos
        y += square_size
        if not check_collision((x, y, horizontal_rect_width, horizontal_rect_height), square_pos) and not check_collision(
                (x, y, horizontal_rect_width, horizontal_rect_height), retangulos_pos):
            horizontal_rect_pos = (x, y)


def check_collision(rect, rects):
    for r in rects:
        if pygame.Rect(rect).colliderect(pygame.Rect(r[0], r[1], square_size, square_size)):
            return True
    return False


def draw_objects():
    screen.fill(WHITE)

    for pos in square_pos:
        pygame.draw.rect(
            screen, RED, (pos[0], pos[1], square_size, square_size))

    for pos in retangulos_pos:
        pygame.draw.rect(
            screen, GREEN, (pos[0], pos[1], retangulo_width, retangulo_height))

    pygame.draw.rect(screen, BLUE, (horizontal_rect_pos[0], horizontal_rect_pos[1],
                                    horizontal_rect_width, horizontal_rect_height))

    pygame.display.update()


# Loop principal do jogo
while True:
    handle_events()
    draw_objects()
