import pygame
from data.classes import *


def main() -> None:
    """main function of the project"""
    pygame.init()
    size = width, height = 1920, 1080
    main_menu = pygame.display.set_mode(size)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    fps = 60

    player_size: int = 20
    v: int = 20
    player: Character = Character(width // 2, height // 2, '#3535F3', player_size, v)

    Wall(0, 0, width - 1, 0, 2)
    Wall(0, 0, 0, height - 1, 2)
    Wall(100, 200, 200, 200, 2)
    Wall(width - 1, 0, width - 3, height - 3, 2)




    main_loop = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_f:
                    ...

        match main_loop:
            case 0:
                main_menu.fill("#121212")
                pygame.draw.rect(main_menu, "#CC3322", pygame.Rect(width // 2 - 150, height // 2 - 40, 300, 80))

            case 1:
                screen.fill("#121212")

                CHARACTER_SPRITES.draw(screen)
                CHARACTER_SPRITES.update()

                WALL_SPRITES.draw(screen)
                WALL_SPRITES.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
