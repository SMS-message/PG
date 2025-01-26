from data.classes import Wall, LevelChanger

w = 240  # distance between walls

walls = (
    Wall(0, w * 2, w * 1, w * 2),
    Wall(w * 1, w * 1, w * 2, w * 1),
    Wall(w * 1, w * 2, w * 1, w * 4),
    Wall(w * 1, w * 4, w * 2, w * 4),
    Wall(w * 2, w * 1, w * 2, w * 2),
    Wall(w * 2, w * 2, w * 3, w * 2),
    Wall(w * 2, w * 2, w * 2, w * 3),
    Wall(w * 3, w * 2, w * 3, w * 3),
    Wall(w * 3, w * 1, w * 4, w * 1),
    Wall(w * 3, 0, w * 3, w * 1),
    Wall(w * 3, w * 3, w * 4, w * 3),
    Wall(w * 3, w * 4, w * 4, w * 4),
    Wall(w * 3, w * 4, w * 3, w * 5),
    Wall(w * 4, w * 2, w * 4, w * 3),
    Wall(w * 4, w * 3, w * 5, w * 3),
    Wall(w * 5, w * 1, w * 5, w * 2),
    Wall(w * 5, w * 1, w * 6, w * 1),
    Wall(w * 5, w * 4, w * 7, w * 4),
    Wall(w * 6, w * 4, w * 6, w * 5),
    Wall(w * 6, 0, w * 6, w * 3),
    Wall(w * 6, w * 2, w * 7, w * 2),
    Wall(w * 7, w * 1, w * 8, w * 1),
    Wall(w * 7, w * 3, w * 8, w * 3),
    LevelChanger(w * 7, 0, w * 8, w * 1)
)
