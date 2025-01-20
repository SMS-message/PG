import pygame
from data.classes import Character, Wall
import data.walls2
from typing import Tuple

pygame.init()
pygame.display.set_caption("EchoMaze")
SIZE = WIDTH, HEIGHT = 120 * 8, 120 * 5
clock = pygame.time.Clock()

main_menu = pygame.display.set_mode(SIZE)


screen = pygame.display.set_mode(SIZE)

FPS = 60
clock.tick(FPS)

PLAYER_SIZE: int = 20
PLAYER_POS: Tuple[int, int] = 20, 20
V: int = 1
player: Character = Character(*PLAYER_POS, '#3535F3', PLAYER_SIZE, V)

main_loop = 1

Wall(0, 0, WIDTH - 1, 0)
Wall(0, 0, 0, HEIGHT - 1)
Wall(WIDTH - 2, 0, WIDTH - 2, HEIGHT - 2)
Wall(0, HEIGHT - 2, WIDTH - 2, HEIGHT - 2)