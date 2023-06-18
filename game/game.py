import pygame

# Definir as dimensões da janela
largura = 200
altura = 250

# Inicializar o Pygame
pygame.init()

# Criar a janela
janela = pygame.display.set_mode((largura, altura))

# Definir a cor azul
azul = (0, 0, 255)

# Definir as dimensões e a posição inicial dos quadrados
tamanho_quadrado = 50
posicao_inicial_x = 0
posicao_y = 0

# Definir as posições dos quadrados
posicoes_quadrados = [
    (posicao_inicial_x, posicao_y),
    (posicao_inicial_x + tamanho_quadrado, posicao_y),
    (posicao_inicial_x + 2 * tamanho_quadrado, posicao_y),
    (posicao_inicial_x + 3 * tamanho_quadrado, posicao_y)
]

# Definir o índice do quadrado atualmente selecionado
quadrado_selecionado = None

# Loop principal do jogo
executando = True
while executando:
    # Verificar se algum evento ocorreu
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Verificar se o botão esquerdo do mouse foi pressionado
                # Verificar se o clique foi em algum quadrado
                pos_mouse = pygame.mouse.get_pos()
                for i, posicao in enumerate(posicoes_quadrados):
                    x, y = posicao
                    if x <= pos_mouse[0] <= x + tamanho_quadrado and y <= pos_mouse[1] <= y + tamanho_quadrado:
                        quadrado_selecionado = i
                        break

        elif evento.type == pygame.KEYDOWN:
            if quadrado_selecionado is not None:
                x, y = posicoes_quadrados[quadrado_selecionado]

                if evento.key == pygame.K_UP:
                    new_y = max(y - tamanho_quadrado, 0)
                    # Verificar se a nova posição não está ocupada por outro quadrado
                    if all((x, new_y) != pos for i, pos in enumerate(posicoes_quadrados) if i != quadrado_selecionado):
                        y = new_y
                elif evento.key == pygame.K_DOWN:
                    new_y = min(y + tamanho_quadrado,
                                altura - tamanho_quadrado)
                    # Verificar se a nova posição não está ocupada por outro quadrado
                    if all((x, new_y) != pos for i, pos in enumerate(posicoes_quadrados) if i != quadrado_selecionado):
                        y = new_y
                elif evento.key == pygame.K_LEFT:
                    new_x = max(x - tamanho_quadrado, 0)
                    # Verificar se a nova posição não está ocupada por outro quadrado
                    if all((new_x, y) != pos for i, pos in enumerate(posicoes_quadrados) if i != quadrado_selecionado):
                        x = new_x
                elif evento.key == pygame.K_RIGHT:
                    new_x = min(x + tamanho_quadrado,
                                largura - tamanho_quadrado)
                    # Verificar se a nova posição não está ocupada por outro quadrado
                    if all((new_x, y) != pos for i, pos in enumerate(posicoes_quadrados) if i != quadrado_selecionado):
                        x = new_x

                # Atualizar a posição do quadrado
                posicoes_quadrados[quadrado_selecionado] = (x, y)

    # Preencher a janela com a cor preta
    janela.fill((0, 0, 0))

    # Desenhar os quadrados azuis
    for posicao in posicoes_quadrados:
        x, y = posicao
        pygame.draw.rect(
            janela, azul, (x, y, tamanho_quadrado, tamanho_quadrado))

    # Atualizar a janela
    pygame.display.update()

# Encerrar o Pygame
pygame.quit()
