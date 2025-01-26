import pygame
from typing import Tuple
from forms.RecordsTable_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3

CHARACTER_SPRITES = pygame.sprite.Group()
WALL_SPRITES = pygame.sprite.Group()
VERTICAL_WALL_SPRITES = pygame.sprite.Group()
HORIZONTAL_WALL_SPRITES = pygame.sprite.Group()
SOUND_SPRITES = pygame.sprite.Group()
LEVEL_CHANGER_SPRITES = pygame.sprite.Group()


class Character(pygame.sprite.Sprite):
    """Character controlled by player"""
    def __init__(self, x: int, y: int, color: tuple[int, int, int] | str, size: int, v: int):
        super().__init__(CHARACTER_SPRITES)
        self.color = color
        self.v = v
        self.vx1, self.vx2, self.vy1, self.vy2 = v, -v, v, -v
        self.size = size

        self.image = pygame.Surface((2 * self.size, 2 * self.size), pygame.SRCALPHA, 32)
        self.image.fill(color)

        self.rect = pygame.Rect(x, y, 2 * size, 2 * size)

    def update(self):
        """
        Character movement and collisions

        :returns: None
        """
        keys = pygame.key.get_pressed()
        collided_ver_wall = pygame.sprite.spritecollideany(self, VERTICAL_WALL_SPRITES)
        collided_hor_wall = pygame.sprite.spritecollideany(self, HORIZONTAL_WALL_SPRITES)
        if collided_ver_wall:
            if collided_ver_wall.x1 > self.rect.x:
                self.vx1 = 0
            else:
                self.vx2 = 0
        else:
            self.vx1, self.vx2 = self.v, -self.v
        if collided_hor_wall:
            if collided_hor_wall.y1 > self.rect.y:
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
    """Walls for structuring mazes"""
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        super().__init__(WALL_SPRITES)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if x1 == x2:
            self.add(VERTICAL_WALL_SPRITES)
            self.image = pygame.Surface([1, y2 - y1])
            self.image.fill(pygame.Color("#CCCCCC"))
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(HORIZONTAL_WALL_SPRITES)
            self.image = pygame.Surface([x2 - x1, 1])
            self.image.fill(pygame.Color("#CCCCCC"))
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

    def delete(self):
        """
        Removes wall for changing levels

        :return: None
        """
        WALL_SPRITES.remove(self)
        VERTICAL_WALL_SPRITES.remove(self)
        HORIZONTAL_WALL_SPRITES.remove(self)
        del self

    def update_group(self):
        """
        adds wall back to group for changing levels

        :return: None
        """
        self.add(WALL_SPRITES)
        if self.x1 == self.x2:
            self.add(VERTICAL_WALL_SPRITES)
        else:
            self.add(HORIZONTAL_WALL_SPRITES)

    def __repr__(self) -> str:
        """
        __repr__ method for debugging

        :return: formated string
        """
        return f"Wall({self.x1}, {self.y1}, {self.x2}, {self.y2})"


class LevelChanger(pygame.sprite.Sprite):
    """Zone, where character should be standing to change level"""
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        super().__init__(LEVEL_CHANGER_SPRITES)
        self.image = pygame.Surface([x2 - x1 - 3, y2 - y1 - 1])
        self.image.fill(pygame.Color("#904040"))
        self.rect = pygame.Rect(x1 + 1, y1 + 1, x2 - x1 - 3, y2 - y1 - 1)

    def delete(self):
        """
        Removes level changing zone for changing levels

        :return: None
        """
        LEVEL_CHANGER_SPRITES.remove(self)
        del self

    def update_group(self):
        """
        adds level changing zone back to group for changing levels

        :return: None
        """
        self.add(LEVEL_CHANGER_SPRITES)

class Sound:
    """Object made for revealing walls"""
    def __init__(self, vx: int, vy: int, center: Tuple[int, int]):
        radius: int = 10
        self.vx, self.vy = vx, vy
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.rect = pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)
        pygame.draw.circle(self.image, pygame.Color("#606060"), center, radius)

    def update(self):
        """
        fills collided wall on touch

        :return: None
        """
        self.rect.move(self.vx, self.vy)
        collided_wall = pygame.sprite.spritecollideany(self, WALL_SPRITES)
        if collided_wall:
            collided_wall.image.fill("#FF0000")
            del self

class RecordsTable(QMainWindow, Ui_MainWindow):
    """PyQt6 window for records table"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("db/records_db.db")
        self.cur = self.con.cursor()

        data = self.cur.execute("""
                                    SELECT (
                                               SELECT seconds
                                                 FROM Time
                                                WHERE id = time_id
                                           ),
                                           level_id
                                      FROM Records;
                                    """)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setColumnCount(2)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(("seconds", "level"))

        self.pushButton.clicked.connect(self.close)
