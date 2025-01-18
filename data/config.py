import pygame
from data.classes import Character
import data.walls

pygame.init()
SIZE = WIDTH, HEIGHT = 1920, 1080
clock = pygame.time.Clock()

main_menu = pygame.display.set_mode(SIZE)

screen = pygame.display.set_mode(SIZE)

FPS = 60
clock.tick(FPS)

PLAYER_SIZE: int = 20
V: int = 1
player: Character = Character(100, 100, '#3535F3', PLAYER_SIZE, V)

main_loop = 0

data.walls.Wall(0, 0, WIDTH - 1, 0)
data.walls.Wall(0, 0, 0, HEIGHT - 1)
data.walls.Wall(WIDTH - 2, 0, WIDTH - 2, HEIGHT - 2)
data.walls.Wall(0, HEIGHT - 2, WIDTH - 2, HEIGHT - 2)