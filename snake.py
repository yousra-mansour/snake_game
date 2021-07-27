import curses
import time
import random


stdscr = curses.initscr()
curses.curs_set(0)  # visibility
sh, sw = stdscr.getmaxyx()  # save

win = curses.newwin(sh, sw, 0, 0)
win.keypad(True)
win.timeout(100)

snk_x = sw//4
snk_y = sh//2

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2],
]

food = [snk_y//2, snk_x//2]
win.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:

    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
    #     curses.endwin
    #     quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:

            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]

            food = nf if nf not in snake else None
        win.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], " ")

    win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)


# for i in range(10):

#     curses.beep()
#     curses.beep()
#     time.sleep(1)
#     curses.beep()
#     time.sleep(.5)
#     curses.beep()
