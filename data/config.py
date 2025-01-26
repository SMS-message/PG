import pygame
from json import load as json_load
from data.classes import Character, Wall
from typing import Tuple

pygame.init()
pygame.display.set_caption("EchoMaze")

with open("data/config.json", encoding="utf-8") as json_file:
    data = json_load(json_file)
    SIZE = WIDTH, HEIGHT = data["game"]["size"]
    clock = pygame.time.Clock()

    MAIN_MENU = pygame.display.set_mode(SIZE)
    LEVEL_TRANSITION = pygame.display.set_mode(SIZE)
    END_MENU = pygame.display.set_mode(SIZE)

    SCREEN = pygame.display.set_mode(SIZE)

    FPS = data["game"]["fps"]
    clock.tick(FPS)

    PLAYER_SIZE: int = data["player"]["size"]
    V: int = data["player"]["speed"]
    PLAYER_POS: Tuple[int, int] = data["player"]["pos"]
    player: Character = Character(*PLAYER_POS, '#3535F3', PLAYER_SIZE, V)

Wall(0, 0, WIDTH - 1, 0)
Wall(0, 0, 0, HEIGHT - 1)
Wall(WIDTH - 2, 0, WIDTH - 2, HEIGHT - 2)
Wall(0, HEIGHT - 2, WIDTH - 2, HEIGHT - 2)
