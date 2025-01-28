import sqlite3

from data.config import *
from data.classes import CHARACTER_SPRITES, WALL_SPRITES, SOUND_SPRITES, LEVEL_CHANGER_SPRITES, RecordsTable
from PyQt6.QtWidgets import QApplication
from sys import argv, exit
from threading import Thread
import datetime as dt

curr_walls = ()
with open("data/config.json", encoding="utf-8") as json_file:
    main_loop = json_load(json_file)["game"]["main_loop"]
with open("data/current_level.txt", mode="r") as f:
    started = f.read() != "0"
running = True
time = dt.datetime.now()

font = pygame.font.SysFont("Arial Black", 84)
game_name = {"render": font.render("EchoMaze", True, "#CCCCCC")}
game_name["pos"] = (WIDTH // 2 - game_name["render"].get_width() // 2,
                    HEIGHT // 2 - game_name["render"].get_height() * 2)

start_button_text = {"render": font.render("Continue" if started else "Start", True, "#CCCCCC", "#303030")}
start_button_text["pos"] = (WIDTH // 2 - start_button_text["render"].get_width() // 2,
                            HEIGHT // 2 - start_button_text["render"].get_height() // 2)

records_start_button_text = {"render": font.render("Records", True, "#CCCCCC", "#303030")}
records_start_button_text["pos"] = (WIDTH // 2 - records_start_button_text["render"].get_width() // 2,
                                    HEIGHT // 2 - records_start_button_text["render"].get_height() // 2 + 150)

exit_start_button_text = {"render": font.render("Exit", True, "#CCCCCC", "#303030")}
exit_start_button_text["pos"] = (WIDTH // 2 - exit_start_button_text["render"].get_width() // 2,
                                 HEIGHT // 2 - exit_start_button_text["render"].get_height() // 2 + 300)

restart_button_text = {"render": font.render("Restart", True, "#CCCCCC", "#303030")}
restart_button_text["pos"] = (WIDTH // 2 - restart_button_text["render"].get_width() // 2,
                              HEIGHT // 2 - restart_button_text["render"].get_height() // 2 - 100)

records_end_button_text = {"render": font.render("Records", True, "#CCCCCC", "#303030")}
records_end_button_text["pos"] = (WIDTH // 2 - records_end_button_text["render"].get_width() // 2,
                                  HEIGHT // 2 - records_end_button_text["render"].get_height() // 2 + 50)

exit_end_button_text = {"render": font.render("Exit", True, "#CCCCCC", "#303030")}
exit_end_button_text["pos"] = (WIDTH // 2 - exit_end_button_text["render"].get_width() // 2,
                               HEIGHT // 2 - exit_end_button_text["render"].get_height() // 2 + 200)

next_level_button_text = {"render": font.render("Next level", True, "#CCCCCC", "#303030")}
next_level_button_text["pos"] = (WIDTH // 2 - next_level_button_text["render"].get_width() // 2,
                                 HEIGHT // 2 - next_level_button_text["render"].get_height() // 2 + 50)


def menu() -> None:
    """
    menu loop

    :returns: None
    """
    global running, main_loop, started, game_name, start_button_text
    mouse_x_on_start_btn: bool = (pygame.mouse.get_pos()[0] in
                                  range(start_button_text["pos"][0],
                                        start_button_text["pos"][0] + start_button_text["render"].get_width()))
    mouse_y_on_start_btn: bool = (pygame.mouse.get_pos()[1] in
                                  range(start_button_text["pos"][1],
                                        start_button_text["pos"][1] + start_button_text["render"].get_height()))
    mouse_x_on_records_btn: bool = (pygame.mouse.get_pos()[0] in
                                    range(records_start_button_text["pos"][0],
                                          records_start_button_text["pos"][0] + records_start_button_text[
                                              "render"].get_width()))
    mouse_y_on_records_btn: bool = (pygame.mouse.get_pos()[1] in
                                    range(records_start_button_text["pos"][1],
                                          records_start_button_text["pos"][1] + records_start_button_text[
                                              "render"].get_height()))
    mouse_x_on_exit_btn: bool = (pygame.mouse.get_pos()[0] in
                                 range(exit_start_button_text["pos"][0],
                                       exit_start_button_text["pos"][0] + exit_start_button_text["render"].get_width()))
    mouse_y_on_exit_btn: bool = (pygame.mouse.get_pos() [1] in
                                 range(exit_start_button_text["pos"][1],
                                       exit_start_button_text["pos"][1] + exit_start_button_text[
                                           "render"].get_height()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                main_loop_transition()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x_on_start_btn and mouse_y_on_start_btn:
                    main_loop_transition()
                elif mouse_x_on_records_btn and mouse_y_on_records_btn:
                    show_records()
                elif mouse_x_on_exit_btn and mouse_y_on_exit_btn:
                    running = False

    started_text = "Start" if not started else "Continue"

    button_hover(mouse_x_on_start_btn and mouse_y_on_start_btn, start_button_text, started_text)
    button_hover(mouse_x_on_records_btn and mouse_y_on_records_btn, records_start_button_text, "Records")
    button_hover(mouse_x_on_exit_btn and mouse_y_on_exit_btn, exit_start_button_text, "Exit")

    MAIN_MENU.fill("#121212")
    MAIN_MENU.blit(*game_name.values())
    MAIN_MENU.blit(*start_button_text.values())
    MAIN_MENU.blit(*records_start_button_text.values())
    MAIN_MENU.blit(*exit_start_button_text.values())


def end_menu() -> None:
    """
    end menu loop

    :returns: None
    """
    global running, main_loop, game_name, restart_button_text

    mouse_x_on_restart_btn: bool = (pygame.mouse.get_pos()[0] in
                                    range(restart_button_text["pos"][0],
                                          restart_button_text["pos"][0] + restart_button_text["render"].get_width()))
    mouse_y_on_restart_btn: bool = (pygame.mouse.get_pos()[1] in
                                    range(restart_button_text["pos"][1],
                                          restart_button_text["pos"][1] + restart_button_text["render"].get_height()))
    mouse_x_on_records_btn: bool = (pygame.mouse.get_pos()[0] in
                                    range(records_end_button_text["pos"][0],
                                          records_end_button_text["pos"][0] +
                                          records_end_button_text["render"].get_width()))
    mouse_y_on_records_btn: bool = (pygame.mouse.get_pos()[1] in
                                    range(records_end_button_text["pos"][1],
                                          records_end_button_text["pos"][1] +
                                          records_end_button_text["render"].get_height()))
    mouse_x_on_exit_btn: bool = (pygame.mouse.get_pos()[0] in
                                 range(exit_end_button_text["pos"][0],
                                       exit_end_button_text["pos"][0] +
                                       exit_end_button_text["render"].get_width()))
    mouse_y_on_exit_btn: bool = (pygame.mouse.get_pos()[1] in
                                 range(exit_end_button_text["pos"][1],
                                       exit_end_button_text["pos"][1] +
                                       exit_end_button_text["render"].get_height()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                with open("data/current_level.txt", mode="w") as file:
                    file.write("1")
                    load_level(1)
                main_loop_transition()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x_on_restart_btn and mouse_y_on_restart_btn:
                    with open("data/current_level.txt", mode="w") as file:
                        file.write("1")
                        load_level(1)
                    main_loop_transition()
                elif mouse_x_on_records_btn and mouse_y_on_records_btn:
                    show_records()
                elif mouse_x_on_exit_btn and mouse_y_on_exit_btn:
                    running = False

    button_hover(mouse_x_on_restart_btn and mouse_y_on_restart_btn, restart_button_text, "Restart")
    button_hover(mouse_x_on_records_btn and mouse_y_on_records_btn, records_end_button_text, "Records")
    button_hover(mouse_x_on_exit_btn and mouse_y_on_exit_btn, exit_end_button_text, "Exit")

    END_MENU.fill("#121212")
    END_MENU.blit(game_name["render"], (game_name["pos"][0], game_name["pos"][1] - 100))
    END_MENU.blit(*restart_button_text.values())
    END_MENU.blit(*records_end_button_text.values())
    END_MENU.blit(*exit_end_button_text.values())


def level_transition_loop() -> None:
    """
    level change loop

    :returns: None
    """
    global running

    mouse_x_on_next_btn: bool = (pygame.mouse.get_pos()[0] in
                                 range(next_level_button_text["pos"][0],
                                       next_level_button_text["pos"][0] +
                                       next_level_button_text["render"].get_width()))
    mouse_y_on_next_btn: bool = (pygame.mouse.get_pos()[1] in
                                 range(next_level_button_text["pos"][1],
                                       next_level_button_text["pos"][1] +
                                       next_level_button_text["render"].get_height()))
    mouse_x_on_exit_btn: bool = (pygame.mouse.get_pos()[0] in
                                 range(exit_start_button_text["pos"][0],
                                       exit_start_button_text["pos"][0] +
                                       exit_start_button_text["render"].get_width()))
    mouse_y_on_exit_btn: bool = (pygame.mouse.get_pos()[1] in
                                 range(exit_start_button_text["pos"][1],
                                       exit_start_button_text["pos"][1] +
                                       exit_start_button_text["render"].get_height()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                with open("data/current_level.txt", mode="w") as file:
                    file.write("2")
                    load_level(2)
                main_loop_transition()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x_on_next_btn and mouse_y_on_next_btn:
                    with open("data/current_level.txt", mode="w") as file:
                        file.write("2")
                    load_level(2)
                    main_loop_transition()
                elif mouse_x_on_exit_btn and mouse_y_on_exit_btn:
                    running = False

    button_hover(mouse_x_on_next_btn and mouse_y_on_next_btn, next_level_button_text, "Next level")
    button_hover(mouse_x_on_exit_btn and mouse_y_on_exit_btn, exit_start_button_text, "Exit")

    LEVEL_TRANSITION.fill("#121212")
    LEVEL_TRANSITION.blit(*game_name.values())
    LEVEL_TRANSITION.blit(*next_level_button_text.values())
    LEVEL_TRANSITION.blit(*exit_start_button_text.values())


def game_loop() -> None:
    """
    main game loop

    :returns: None
    """
    global main_loop, running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_loop = 0
            if event.key == pygame.K_f:
                player.make_sound()

    SCREEN.fill("#121212")

    LEVEL_CHANGER_SPRITES.draw(SCREEN)
    LEVEL_CHANGER_SPRITES.update()

    CHARACTER_SPRITES.draw(SCREEN)
    CHARACTER_SPRITES.update()

    WALL_SPRITES.draw(SCREEN)
    WALL_SPRITES.update()

    SOUND_SPRITES.draw(SCREEN)
    SOUND_SPRITES.update()

    if pygame.sprite.spritecollideany(player, LEVEL_CHANGER_SPRITES):
        with open("data/current_level.txt", mode="r") as file:
            level = int(file.read())
            if level == 1:
                main_loop = 2
            else:
                main_loop = 3
        player.rect = pygame.Rect(*PLAYER_POS, 2 * PLAYER_SIZE, 2 * PLAYER_SIZE)


def game_cycle() -> None:
    """
    standard pygame game cycle

    :returns: None
    """
    global started, running, game_name, start_button_text
    with open("data/current_level.txt", mode="r") as file:
        level = int(file.read())
        level = 1 if not level else level
        load_level(level)
    with open("data/current_level.txt", mode="w") as file:
        file.write(str(level))
    while running:
        match main_loop:
            case 0:
                menu()
            case 1:
                game_loop()
            case 2:
                level_transition_loop()
            case 3:
                end_menu()
        pygame.display.flip()
    terminate()


def main_loop_transition() -> None:
    """
    changing main loop to game loop

    :returns: None
    """
    global start_button_text, main_loop, started
    main_loop = 1
    started = True
    start_button_text = {"render": font.render("Continue", True, "#CCCCCC", "#303030")}
    start_button_text["pos"] = (WIDTH // 2 - start_button_text["render"].get_width() // 2,
                                HEIGHT // 2 - start_button_text["render"].get_height() // 2)


def load_level(level: int) -> None:
    """
    loads level starting from 0 - menu to 2 - last level

    :param level: level id
    :returns: None
    """
    global curr_walls, time
    delta: dt.timedelta = dt.datetime.now() - time
    if delta.seconds != 0:
        con = sqlite3.connect("db/records_db.db")
        cur = con.cursor()
        cur.execute(f"""
                        INSERT INTO Time (
                                         seconds
                                     )
                                     VALUES (
                                         '{delta.seconds}'
                                     )""")
        max_id = max(cur.execute('''
                                    SELECT ID
                                      FROM time;
                                '''))[0]
        cur.execute(f"""
                        INSERT INTO Records (
                                                time_id,
                                                level_id
                                            )
                                            VALUES (
                                                '{max_id}',
                                                '{level - 1 if level == 2 else level + 1}'
                                            );
                    """)
        con.commit()
    match level:
        case 1:
            for wall in curr_walls:
                if isinstance(wall, Wall):
                    wall.image.fill("#121212")
                wall.delete()
            from levels.walls import walls as curr_walls
            for wall in curr_walls:
                wall.update_group()
        case 2:
            for wall in curr_walls:
                if isinstance(wall, Wall):
                    wall.image.fill("#121212")
                wall.delete()
            from levels.walls2 import walls as curr_walls
            for wall in curr_walls:
                wall.update_group()
    time = dt.datetime.now()


def button_hover(mouse_on_btn: bool, btn_text: dict, render_text: str) -> None:
    """
    Changes background color of a button on hover

    :param mouse_on_btn: is mouse on a button
    :param btn_text: dictionary with info of button
    :param render_text: text to be rendered
    :returns: None
    """
    if mouse_on_btn:
        btn_text["render"] = font.render(render_text, True, "#FFFFFF", "#454545")
    else:
        btn_text["render"] = font.render(render_text, True, "#CCCCCC", "#303030")


def to_second_thread(func):
    """
    Adding function to the second thread

    :param func: function for wrapping
    :returns: changed function
    """

    def wrapper():
        sec_thread = Thread(target=func)
        sec_thread.start()

    return wrapper


@to_second_thread
def show_records() -> None:
    """
    show records window

    :returns: None
    """
    try:
        app = QApplication(argv)
        ex = RecordsTable()
        ex.show()
        exit(app.exec())
    except Exception as err:
        print(err)


def terminate() -> None:
    """
    ends the game

    :returns: None
    """
    pygame.quit()
    exit()
