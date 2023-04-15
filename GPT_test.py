import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
screen_width = 400
screen_height = 400

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Анимация бегающего человечка")

# Загрузка изображений человечка
running_images = [pygame.image.load("run1.png"),
                  pygame.image.load("run2.png"),
                  pygame.image.load("run3.png"),
                  pygame.image.load("run4.png")]
jumping_image = pygame.image.load("jump.png")

# Изначальные координаты и состояние человечка
x = 50
y = screen_height - 150
is_jumping = False
jump_height = 10
jump_count = 0

# Основной цикл анимации
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление состояния человечка
    if not is_jumping:
        x += 5
        if x > screen_width:
            x = -100

    # Обновление состояния прыжка
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовка человечка
    if is_jumping:
        screen.blit(jumping_image, (x, y))
    else:
        screen.blit(running_images[x // 8 % 4], (x, y))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(60)
