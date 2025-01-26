from data.classes import Wall, LevelChanger

w = 240  # distance between walls

walls = (
    Wall(w * 1, 0, w * 1, w * 1),
    Wall(w * 1, w * 1, 2 * w, w * 1),
    Wall(w * 1, w * 2, 2 * w, 2 * w),
    Wall(w * 1, 2 * w, 2 * w, 2 * w),
    Wall(w * 1, 2 * w, w * 1, 3 * w),
    Wall(0, 4 * w, w * 1, 4 * w),
    Wall(2 * w, 2 * w, 2 * w, 4 * w),
    Wall(2 * w, 3 * w, 3 * w, 3 * w),
    Wall(3 * w, w * 1, 3 * w, 5 * w),
    Wall(3 * w, 2 * w, 4 * w, 2 * w),
    Wall(4 * w, 0, 4 * w, w * 1),
    Wall(4 * w, w * 1, 6 * w, w * 1),
    Wall(4 * w, 3 * w, 7 * w, 3 * w),
    Wall(4 * w, 3 * w, 4 * w, 4 * w),
    Wall(5 * w, 2 * w, 5 * w, 3 * w),
    Wall(5 * w, 4 * w, 5 * w, 5 * w),
    Wall(5 * w, 4 * w, 6 * w, 5 * w),
    Wall(6 * w, w * 1, 6 * w, 2 * w),
    Wall(6 * w, 2 * w, 7 * w, 2 * w),
    Wall(7 * w, 2 * w, 7 * w, 4 * w),
    Wall(7 * w, w * 1, 8 * w, w * 1),
    LevelChanger(w * 4, 0, w * 5, w * 1)
)
