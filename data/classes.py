import pygame

CHARACTER_SPRITES = pygame.sprite.Group()
WALL_SPRITES = pygame.sprite.Group()


class Character(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, color: tuple[int, int, int] | str, size: int, v: int):
        super().__init__(CHARACTER_SPRITES)
        self.x, self.y = x, y
        self.color = color
        self.v = v
        self.size = size

        self.image = pygame.Surface((2 * self.size, 2 * self.size), pygame.SRCALPHA, 32)
        self.image.fill(color)

        self.rect = pygame.Rect(x, y, 2 * size, 2 * size)

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, -self.v)
        if keys[pygame.K_s]:
            self.rect = self.rect.move(0, self.v)
        if keys[pygame.K_a]:
            self.rect = self.rect.move(-self.v, 0)
        if keys[pygame.K_d]:
            self.rect = self.rect.move(self.v, 0)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, width: int):
        super().__init__(WALL_SPRITES)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.image = pygame.Surface(((x2 - x1) + width, (y2 - y1) + width))
        self.image.fill('#CCCCCC')
        self.rect = self.image.get_rect()



class Sound:
    ...
