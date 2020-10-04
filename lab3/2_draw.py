import pygame
from pygame.draw import *


def leg(screen: pygame.display, cord_x: int, cord_y: int, size: float,
        colour_body: tuple):
    ellipse(screen, colour_body, (round(cord_x - size * 10), round(cord_y - size * 24),
                                  round(size * 2 * 10), round(size * 2 * 24)))
    ellipse(screen, colour_body, (round(cord_x - size * 10), round(cord_y + size * 24 - size * 5),
                                  round(size * 2 * 10), round(size * 2 * 24)))
    ellipse(screen, colour_body, (round(cord_x + size * 5 - size * 10), round(cord_y + size * 71 - size * 7),
                                  round(size * 2 * 10), round(size * 2 * 7)))


def eye(screen: pygame.display, cord_x: int, cord_y: int, size: float,
        colour_body: tuple, colour_eye_1: tuple, colour_eye_2: tuple):
    ellipse(screen, colour_eye_2,
            ((cord_x + round(size * 64)) - round(size * 12), (cord_y - round(size * 128) - round(size * 10)),
             round(size * 2 * 12), round(size * 2 * 10)))
    ellipse(screen, colour_eye_1,
            ((cord_x + round(size * 70) - round(size * 5), (cord_y - round(size * 129)) - round(size * 4),
              round(size * 2 * 5), round(size * 2 * 4))))
    surface = pygame.Surface((round(size * 12), round(size * 6)), pygame.SRCALPHA)
    ellipse(surface, colour_body, (0, 0, round(size * 11), round(size * 5)))
    surface_rot = pygame.transform.rotate(surface, -30)
    screen.blit(surface_rot, (cord_x + round(size * 58), cord_y - round(size * 138)))


def body(screen: pygame.display, cord_x: int, cord_y: int, size: float,
         colour_body: tuple):
    ellipse(screen, colour_body,
            (cord_x - round(size * 68), cord_y - round(size * 32),
             round(size * 2 * 68), round(size * 2 * 32)))
    ellipse(screen, colour_body,
            ((cord_x + round(size * 57)) - round(size * 19), (cord_y - round(size * 64)) - round(size * 52),
             round(size * 2 * 19), round(size * 2 * 52)))
    ellipse(screen, colour_body,
            ((cord_x + round(size * 67)) - round(size * 24), (cord_y - round(size * 124)) - round(size * 16),
             round(size * 2 * 24), round(size * 2 * 16)))


def ears(screen: pygame.display, cord_x: int, cord_y: int, size: float,
         colour_body: tuple):
    ear_1_points_1 = []
    ear_1_points_2 = []
    ear_2_points_1 = []
    ear_2_points_2 = []

    for i in range(round(size * 14)):
        ear_1_points_1.append(
            (i, round(-round(size * 19) / round(size * 14) ** 2 * (i - round(size * 14)) ** 2 + round(size * 19))))
        ear_1_points_2.append(
            (i, round(-round(size * 14) / round(size * 14) ** 2 * (i - round(size * 14)) ** 2 + round(size * 14))))
    surface_1 = pygame.Surface((round(size * 18), round(size * 24)), pygame.SRCALPHA)
    polygon(surface_1, colour_body, ear_1_points_1 + ear_1_points_2[::-1])
    screen.blit(surface_1, [round(cord_x + size * 40), round(cord_y - size * 151)])

    for i in range(round(size * 17)):
        ear_2_points_1.append(
            (i, round(-round(size * 15) / round(size * 24) ** 2 * (i - round(size * 24)) ** 2 + round(size * 15))))
        ear_2_points_2.append(
            (i, round(-round(size * 17) / round(size * 18) ** 2 * (i - round(size * 18)) ** 2 + round(size * 17))))
    surface_2 = pygame.Surface((round(size * 17), round(size * 24)), pygame.SRCALPHA)
    polygon(surface_2, colour_body, ear_2_points_1 + ear_2_points_2[::-1])
    screen.blit(surface_2, [round(cord_x + size * 33), round(cord_y - size * 147)])


def llama(screen: pygame.display, cord_x: int, cord_y: int, size: float,
          colour_body: tuple, colour_eye_1: tuple, colour_eye_2: tuple):
    ears(screen, cord_x, cord_y, size, colour_body)

    body(screen, cord_x, cord_y, size, colour_body)

    leg(screen, cord_x + round(size * 45), cord_y + round(size * 38), size, colour_body)
    leg(screen, cord_x - round(size * 25), cord_y + round(size * 38), size, colour_body)
    leg(screen, cord_x - round(size * 51), cord_y + round(size * 13), size, colour_body)
    leg(screen, cord_x + round(size * 23), cord_y + round(size * 13), size, colour_body)

    eye(screen, cord_x, cord_y, size, colour_body, colour_eye_1, colour_eye_2)


def flower(screen: pygame.display, cord_x: int, cord_y: int, size: float, angle: float,
           colour_flower_1: tuple, colour_flower_2: tuple, colour_flower_3: tuple):
    surface = pygame.Surface((round(size * 49), round(size * 26)), pygame.SRCALPHA)

    ellipse(surface, colour_flower_1, (round(size * 18 - size * 8), round(size * 6 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)))
    ellipse(surface, colour_flower_3, (round(size * 18 - size * 8), round(size * 6 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)), round(size))

    ellipse(surface, colour_flower_1, (round(size * 30 - size * 8), round(size * 5 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)))
    ellipse(surface, colour_flower_3, (round(size * 30 - size * 8), round(size * 5 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)), round(size))

    ellipse(surface, colour_flower_2, (round(size * 25 - size * 11), round(size * 10 - size * 4),
                                       round(size * 2 * 11), round(size * 2 * 4)))

    ellipse(surface, colour_flower_1, (round(size * 35 - size * 8), round(size * 10 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)))
    ellipse(surface, colour_flower_3, (round(size * 35 - size * 8), round(size * 10 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)), round(size))

    ellipse(surface, colour_flower_1, (round(size * 13 - size * 8), round(size * 12 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)))
    ellipse(surface, colour_flower_3, (round(size * 13 - size * 8), round(size * 12 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)), round(size))

    ellipse(surface, colour_flower_1, (round(size * 22 - size * 8), round(size * 16 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)))
    ellipse(surface, colour_flower_3, (round(size * 22 - size * 8), round(size * 16 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)), round(size ))

    ellipse(surface, colour_flower_1, (round(size * 30 - size * 8), round(size * 15 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)))
    ellipse(surface, colour_flower_3, (round(size * 30 - size * 8), round(size * 15 - size * 5),
                                       round(size * 2 * 8), round(size * 2 * 5)), round(size))

    surface_rot = pygame.transform.rotate(surface, angle)
    screen.blit(surface_rot, (cord_x - round(size * 27), cord_y - round(size * 13)))


def bush(screen: pygame.display, cord_x: int, cord_y: int, size: float,
         colour_bush: tuple, colour_flower_1: tuple, colour_flower_2: tuple, colour_flower_3: tuple):
    ellipse(screen, colour_bush, (cord_x - round(size * 115), cord_y - round(size * 115),
                                  round(size * 2 * 115), round(size * 2 * 115)))
    flower(screen, cord_x + round(size * 10), cord_y - round(size * 60), size + 1, 0,
           colour_flower_1, colour_flower_2, colour_flower_3)
    flower(screen, cord_x - round(size * 65), cord_y - round(size * 30), size + 0.5, 20,
           colour_flower_1, colour_flower_2, colour_flower_3)
    flower(screen, cord_x - round(size * 55), cord_y + round(size * 10), size + 1, 30,
           colour_flower_1, colour_flower_2, colour_flower_3)
    flower(screen, cord_x + round(size * 15), cord_y + round(size * 40), size + 1, -30,
           colour_flower_1, colour_flower_2, colour_flower_3)
    flower(screen, cord_x + round(size * 60), cord_y - round(size * 20), size + 1, -50,
           colour_flower_1, colour_flower_2, colour_flower_3)


def main():
    pygame.init()

    pixels_x = 600  # Количество пикселей в картинке по горизонтали
    pixels_y = 900  # Количетво пикселей в картинке по вертикали
    FPS = 30
    screen = pygame.display.set_mode((pixels_x, pixels_y))

    # Задание цветовых кортежей, нужных в рисунке
    CYAN = (175, 221, 233)
    GREY = (179, 179, 179)
    GREEN = (170, 222, 135)
    BLACK = (0, 0, 0)
    VIOLET = (229, 128, 255)
    WHITE = (255, 255, 255)
    DARK_GREEN = (113, 200, 55)
    YELLOW = (255, 255, 0)

    # Заполнение всего экрана зелёным цветом, чтобы потом на него наложить небо и горы
    screen.fill(GREEN)

    # Прорисовка неба
    rect(screen, CYAN, (0, 0, pixels_x, 450))

    # Захардкоженная прорисовка гор, высчитывал в пеинте нижнюю линию, затем рисование контура
    # Извините за множество чисел :)
    polygon(screen, GREY, [(-1, 280), (70, 89), (125, 220), (205, 120), (358, 361), (468, 111), (503, 156), (601, 34),
                           (601, 533), (351, 533), (339, 528), (336, 526), (336, 526), (336, 481), (333, 478),
                           (333, 462),
                           (327, 453), (322, 453), (315, 450), (132, 450), (75, 460), (56, 460), (29, 463), (0, 476)])
    polygon(screen, BLACK, [(-1, 280), (70, 89), (125, 220), (205, 120), (358, 361), (468, 111), (503, 156), (601, 34),
                            (601, 533), (351, 533), (339, 528), (336, 526), (336, 526), (336, 481), (333, 478),
                            (333, 462),
                            (327, 453), (322, 453), (315, 450), (132, 450), (75, 460), (56, 460), (29, 463), (0, 476)],
            1)

    # Рисование одной ламы в определённых координатах с определёнными линейными размерами (за единицу взяты размеры ламы
    # с боевого задания)
    llama(screen, 143, 593, 1, WHITE, BLACK, VIOLET)

    bush(screen, 503, 740, 1, DARK_GREEN, WHITE, YELLOW, GREY)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


main()
