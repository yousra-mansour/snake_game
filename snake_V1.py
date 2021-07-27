import curses
import random

while True :

    lifes = 4
    stdscr = curses.initscr()
    curses.curs_set(0)  # visibility
    sh, sw = stdscr.getmaxyx()  # save
    win = curses.newwin(sh, sw, 0, 0)
    print(sw, " ", sh)
    win.keypad(True)
    win.timeout(100)
    win.hline(2, 2, "~", sw - 4)
    win.vline(2, 2, "~", sh - 3)
    win.hline(sh - 2, 2, "~", sw - 4)
    win.vline(2, sw - 4, "~", sh - 3)

    win.insstr(0, 1, "Life: ")
    for i in [7, 10, 13]:
        win.addch(0, i, 1, curses.ACS_DIAMOND)


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

    def check_lifes(lifes):
        if lifes == 3:
            win.addch(0, 13, " ")
        elif lifes == 2:
            win.addch(0, 10, " ")
        elif lifes == 1:
            win.addch(0, 7, " ")
        if lifes == 0:
            snake.clear()
            win.erase()
            win.refresh()
            curses.napms(100)
            win.insstr(sh//2 - 2, sw//2 - 5, "Game Over")
            win.refresh()
            curses.napms(3000)
            curses.endwin
            quit()

    scoure = 0
    win.insstr(0, sw - 20, f"Score: {scoure}\t\t\t")
    def print_score(scoure):
        win.insstr(0, sw - 20, f"Score: {scoure}\t\t\t")


    while True:

        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:



        if snake[0][0] in [2, sh - 2] or snake[0][1] in [2, sw - 4] or snake[0] in snake[1:]:

            lifes -= 1
            curses.beep()
            if snake[0][0] in [2, sh - 2] :
                if sh - snake[0][0] - 1 > 0:
                    snake[0][0] = sh - snake[0][0] 
                else:
                    snake[0][0] = sh - snake[0][0] - 1
            elif snake[0][1] in [2, sw - 4]:
                if sw - 5 - snake[0][1] > 0:
                    snake[0][1] = sw - 5 - snake[0][1]
                else:
                    snake[0][1] = sw - snake[0][1] 


            check_lifes(lifes)


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
            scoure +=1
            print_score(scoure)
            
            while food is None:

                nf = [
                    random.randint(3, sh - 3),
                    random.randint(3, sw - 5)
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
