import pygame
import sys
import math
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Creatures")

# Создание объекта для отслеживания времени
clock = pygame.time.Clock()

# Класс для представления существ
class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle
        self.speed = 2  # Медленная скорость движения
        self.life_cycle = 0

    def update(self):
        self.life_cycle += 1

        if self.life_cycle <= 300:  # Жизненный цикл существа - 10 секунд (300 кадров при 60 FPS)
            # Изменение траектории движения на 1-2 градуса случайным образом
            self.angle += math.radians(random.randint(-25, 25))

            # Обновление координат на основе угла и скорости
            self.rect.x += self.speed * math.cos(self.angle)
            self.rect.y -= self.speed * math.sin(self.angle)

            # Проверка на выход за пределы экрана и обновление координат, если это произошло
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
        else:
            # Создание потомка, если жизненный цикл существа достиг половины
            if self.life_cycle == 150:  # Изменено на половину жизненного цикла (300 / 2)
                child = Creature(self.rect.x, self.rect.y, self.angle)
                creatures.add(child)

            # Удаление существа, если его жизненный цикл закончен
            if self.life_cycle >= 300:
                self.kill()

# Создание группы спрайтов для всех существ
creatures = pygame.sprite.Group()

# Создание начальных существ
for i in range(10):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    angle = math.radians(random.randint(0, 360))
    creature = Creature(x, y, angle)
    creatures.add(creature)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)  # Очистка экрана

    # Обновление и отрисовка всех спрайтов существ
    for creature in creatures:
        creature.update()

        # Создание потомка в середине жизненного цикла
        if creature.life_cycle == 150:
            offspring = Creature(creature.rect.centerx, creature.rect.centery, creature.angle)
            creatures.add(offspring)

        # Удаление существа, если его жизненный цикл завершен
        if creature.life_cycle >= 300:
            creature.kill()

    creatures.draw(screen)  # Отрисовка существ на экране

    # Отображение счетчика существ в верхнем левом углу экрана
    font = pygame.font.Font(None, 36)
    count_text = font.render("Count: {}".format(len(creatures)), True, WHITE)
    screen.blit(count_text, (10, 10))

    pygame.display.flip()  # Отображение обновленного экрана
    clock.tick(60)  # Ограничение FPS до 60