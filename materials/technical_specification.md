# Техническое задание

1. Project Name: Лабиринт с эхолокацией
2. Authors:
    - Team Lead: Чагаев Егор Алексеевич.
    - Project Developers: Чагаев Егор Алексеевич (пока я один)
    - Teacher: Анатольев Алексей Владимирович
3. Description of the program.
    - Запуск и главное меню
   > - Запуск игры производится через файл main.py или main.exe;
   > - Главное меню включает в себя кнопки: старт, выход из игры, таблицу рекордов, а также текст с названием самой игры.
    - Завершение игры и финальное окно
   > - При выходе из лабиринта появляется окно, где пользователю будет предложено пройти лабиринт ещё раз;
   > - В финальном окне можно будет увидеть насколько быстро игрок прошёл лабиринт.
    - Управление персонажем и объекты
   > - Камера находится сверху, так что персонаж может двигаться вперёд, назад, влево и вправо;
   > - Изначально стенки лабиринта не видно, но чтобы их отобразить надо "издать звук";
   > - Нажав на отдельную кнопку персонаж может "издать звук" - выпустить некое количество объектов, которые при
       попадании в стенку прилепляются к ней;
   > - Таким образом можно будет увидеть стенки лабиринта.
    - Взаимодействие объектов и персонажа
   > - Персонаж обладает коллизией, т. е. не может проходить сквозь стены;
   > - "звук" может прилипнуть к стене;
   > - "звук" и персонаж могут проходить сквозь друг-друга.
4. Project Description.
    - Структура проекта:
   > - Готовый проект запускается из файла "main.py" или "main.exe";
   > - Импортируем все нужные нам классы и функции из /data/;
   > - Схема работы ![](scheme_of_work.png)
5. Program code plan.
    - Функции и декораторы:
   > main(), game_cycle(), game_loop(), menu(), end_menu(), level_transition_loop(), main_loop_transition(), load_level(), button_hover(), to_second_thread(), show_records(), terminate();
    - Классы:
   > Character, LevelChanger, Sound, Wall, RecordsTable;
    - Библиотеки:
   > pygame, PyQt6, json, sqlite3, threading.
6. Graphical interface.
    ![](graphical_interface1.png)
    ![](graphical_interface2.png)
7. Deadlines.

   | Задача                                     | Дедлайн          |
   |--------------------------------------------|------------------|
   | Создание команд, описание проекта          | 8 декабря 23:59  |
   | Задание ТЗ (technical_specification.md)    | 15 декабря 23:59 |
   | Часть задания сделана                      | 22 декабря 23:59 |
   | Работающая часть проекта                   | 29 декабря 23:59 |
   | Черновик пояснительной записки (README.md) | 19 января 23:59  |
   | Презентация                                | 26 января 23:59  |
   | Всё готово к вечеру перед защитой          | 2 февраля 23:59  |
   | Защита                                     | 3 февраля        |
