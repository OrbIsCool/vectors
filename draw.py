import pygame

pygame.init()
SCREEN_DIM = (1920, 1080)
screen = pygame.display.set_mode(SCREEN_DIM)


def points(x1, y1, x2, y2, color=(100, 100, 100)):
    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(
            min(x1, x2),
            min(y1, y2),
            max(x1, x2) - min(x1, x2),
            max(y1, y2) - min(y1, y2),
        ),
    )


def center_size(x, y, sizex, sizey, color=(100, 100, 100)):
    pygame.draw.rect(
        screen, color, pygame.Rect(x - sizex / 2, y - sizey / 2, sizex, sizey)
    )


def line_points(x1, y1, x2, y2, width=3, color=(100, 100, 100)):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)


def line_posdir(x, y, ang, size, color=(100, 100, 100)):
    pass
