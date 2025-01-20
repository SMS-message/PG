from data.classes import Wall

w = 240  # Расстояние между стенами

walls = (
    Wall(w, 0, w, w),
    Wall(w, w, 2 * w, w),
    Wall(w, 2 * w, 2 * w, 2 * w),
    Wall(w, 2 * w, 2 * w, 2 * w),
    Wall(w, 2 * w, w, 3 * w),
    Wall(0, 4 * w, w, 4 * w),
    Wall(2 * w, 2 * w, 2 * w, 4 * w),
    Wall(2 * w, 3 * w, 3 * w, 3 * w),
    Wall(3 * w, w, 3 * w, 5 * w),
    Wall(3 * w, 2 * w, 4 * w, 2 * w),
    Wall(4 * w, 0, 4 * w, w),
    Wall(4 * w, w, 6 * w, w),
    Wall(4 * w, 3 * w, 7 * w, 3 * w),
    Wall(4 * w, 3 * w, 4 * w, 4 * w),
    Wall(5 * w, 2 * w, 5 * w, 3 * w),
    Wall(5 * w, 4 * w, 5 * w, 5 * w),
    Wall(5 * w, 4 * w, 6 * w, 5 * w),
    Wall(6 * w, w, 6 * w, 2 * w),
    Wall(6 * w, 2 * w, 7 * w, 2 * w),
    Wall(7 * w, 2 * w, 7 * w, 4 * w),
    Wall(7 * w, w, 8 * w, w),
)
