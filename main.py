import pygame
from data.classes import *


def main() -> None:
    """main function of the project"""
    pygame.init()
    size = width, height = 1920, 1080
    clock = pygame.time.Clock()

    main_menu = pygame.display.set_mode(size)

    font = pygame.font.SysFont("Arial Black", 84)
    name: dict = {"render": font.render("EchoMaze", True, "#CCCCCC")}
    name["pos"] = (width // 2 - name["render"].get_width() // 2, height // 2 - name["render"].get_height() * 2)


    start_text: dict = {"render": font.render("Start", True, "#CCCCCC", "#303030")}
    start_text["pos"] = (width // 2 - start_text["render"].get_width() // 2,
                         height // 2 - start_text["render"].get_height() // 2)
    started: bool = False

    screen = pygame.display.set_mode(size)

    fps = 60

    player_size: int = 20
    v: int = 5
    player: Character = Character(width // 2, height // 2, '#3535F3', player_size, v)

    Wall(0, 0, width - 1, 0)
    Wall(0, 0, 0, height - 1)
    Wall(width - 2, 0, width - 2, height - 2)
    Wall(0, height - 2, width - 2, height - 2)

    Wall(1000, 500, 1500, 500)

    running = True
    main_loop = 0

    while running:
        match main_loop:
            case 0:
                mouse_x_on_btn: bool = (pygame.mouse.get_pos()[0] in
                                        range(start_text["pos"][0],
                                              start_text["pos"][0] + start_text["render"].get_width()))
                mouse_y_on_btn: bool = (pygame.mouse.get_pos()[1] in
                                        range(start_text["pos"][1],
                                              start_text["pos"][1] + start_text["render"].get_height()))
                started_text = "Start" if not started else "Continue"
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 and mouse_x_on_btn and mouse_y_on_btn:
                            main_loop = 1
                            started: bool = True
                            start_text: dict = {"render": font.render("Continue", True, "#CCCCCC", "#303030")}
                            start_text["pos"] = (width // 2 - start_text["render"].get_width() // 2,
                                                 height // 2 - start_text["render"].get_height() // 2)

                if mouse_x_on_btn and mouse_y_on_btn:
                    start_text["render"] = font.render(started_text, True, "#FFFFFF", "#454545")
                else:
                    start_text["render"] = font.render(started_text, True, "#CCCCCC", "#303030")

                main_menu.fill("#121212")
                main_menu.blit(*name.values())
                main_menu.blit(*start_text.values())

            case 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            main_loop = 0
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
