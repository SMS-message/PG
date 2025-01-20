import pygame
from typing import Tuple

CHARACTER_SPRITES = pygame.sprite.Group()
WALL_SPRITES = pygame.sprite.Group()
VERTICAL_WALL_SPRITES = pygame.sprite.Group()
HORIZONTAL_WALL_SPRITES = pygame.sprite.Group()
SOUND_SPRITES = pygame.sprite.Group()


class Character(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, color: tuple[int, int, int] | str, size: int, v: int):
        super().__init__(CHARACTER_SPRITES)
        self.color = color
        self.v = v
        self.vx1, self.vx2, self.vy1, self.vy2 = v, -v, v, -v
        self.size = size

        self.image = pygame.Surface((2 * self.size, 2 * self.size), pygame.SRCALPHA, 32)
        self.image.fill(color)

        self.rect = pygame.Rect(x, y, 2 * size, 2 * size)

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        collided_ver_wall = pygame.sprite.spritecollideany(self, VERTICAL_WALL_SPRITES)
        collided_hor_wall = pygame.sprite.spritecollideany(self, HORIZONTAL_WALL_SPRITES)
        if collided_ver_wall:
            if collided_ver_wall.x > self.rect.x:
                self.vx1 = 0
            else:
                self.vx2 = 0
        else:
            self.vx1, self.vx2 = self.v, -self.v
        if collided_hor_wall:
            if collided_hor_wall.y > self.rect.y:
                self.vy1 = 0
            else:
                self.vy2 = 0
        else:
            self.vy1, self.vy2 = self.v, -self.v
        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, self.vy2)
        if keys[pygame.K_s]:
            self.rect = self.rect.move(0, self.vy1)
        if keys[pygame.K_a]:
            self.rect = self.rect.move(self.vx2, 0)
        if keys[pygame.K_d]:
            self.rect = self.rect.move(self.vx1, 0)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        super().__init__(WALL_SPRITES)
        self.x = x1
        self.y = y1
        if x1 == x2:
            self.add(VERTICAL_WALL_SPRITES)
            self.image = pygame.Surface([1, y2 - y1])
            self.image.fill("#CCCCCC")
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(HORIZONTAL_WALL_SPRITES)
            self.image = pygame.Surface([x2 - x1, 1])
            self.image.fill("#CCCCCC")
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Sound:
    def __init__(self, vx: int, vy: int, center: Tuple[int, int]):
        radius: int = 10
        self.vx, self.vy = vx, vy
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.rect = pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)
        pygame.draw.circle(self.image, pygame.Color("#606060"), center, radius)

    def update(self):
        self.rect.move(self.vx, self.vy)
        collided_wall = pygame.sprite.spritecollideany(self, WALL_SPRITES)
        if collided_wall:
            collided_wall.image.fill("#FF0000")
            del self