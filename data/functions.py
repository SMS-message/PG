from data.config import *
from data.classes import CHARACTER_SPRITES, WALL_SPRITES

font = pygame.font.SysFont("Arial Black", 84)
name = {"render": font.render("EchoMaze", True, "#CCCCCC")}
name["pos"] = (WIDTH // 2 - name["render"].get_width() // 2, HEIGHT // 2 - name["render"].get_height() * 2)

start_text = {"render": font.render("Start", True, "#CCCCCC", "#303030")}
start_text["pos"] = (WIDTH // 2 - start_text["render"].get_width() // 2,
                     HEIGHT // 2 - start_text["render"].get_height() // 2)

started = False
running = True


def menu():
    global running, main_loop, started, name, start_text, font
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
                started = True
                start_text = {"render": font.render("Continue", True, "#CCCCCC", "#303030")}
                start_text["pos"] = (WIDTH // 2 - start_text["render"].get_width() // 2,
                                     HEIGHT // 2 - start_text["render"].get_height() // 2)

    if mouse_x_on_btn and mouse_y_on_btn:
        start_text["render"] = font.render(started_text, True, "#FFFFFF", "#454545")
    else:
        start_text["render"] = font.render(started_text, True, "#CCCCCC", "#303030")

    main_menu.fill("#121212")
    main_menu.blit(*name.values())
    main_menu.blit(*start_text.values())


def game_loop():
    global main_loop, running
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


def game_cycle():
    global started, running, name, start_text

    while running:
        match main_loop:
            case 0:
                menu()
            case 1:
                game_loop()
        pygame.display.flip()
    terminate()


def terminate():
    pygame.quit()
    quit()
