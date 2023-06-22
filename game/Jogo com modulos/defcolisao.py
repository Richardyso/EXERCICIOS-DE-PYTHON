def check_collision(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    # Verificar colisão entre retângulos
    if x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:
        return True

    # Verificar colisão entre retângulo e quadrado
    if isinstance(rect1, tuple) and isinstance(rect2, list):
        rx, ry, rw, rh = rect1
        qx, qy, qs = rect2

        if rx < qx + qs and rx + rw > qx and ry < qy + qs and ry + rh > qy:
            return True

    return False
