import curses
import time
import random

win = curses.initscr()
def game():
    win.nodelay(1)
    curses.curs_set(0)
    win.keypad(1)
    curses.noecho()
    win.border(0)
    scr_size = win.getmaxyx()
    head = [scr_size[0] // 2, 1]
    body = [head[:]] * 20
    direction = 0       # 0: right, 1: down, 2:left, 3:up
    game_over = 0
    tail = body[-1][:]
    food = 0
    score = 0

    while game_over == 0:
        if tail not in body:
            win.addch(tail[0], tail[1], " ")

        win.addstr(0, scr_size[1] // 2 - len("..:: S  N  A  K  E ::..") // 2,
        "..:: S  N  A  K  E ::..",curses.A_REVERSE | curses.A_UNDERLINE)
        win.addstr(0, 0, "SCORE: " + str(score), curses.A_BOLD)

        button = win.getch()
        if button == curses.KEY_RIGHT and direction != 2:
            direction = 0
        elif button == curses.KEY_DOWN and direction != 3:
            direction = 1
        elif button == curses.KEY_LEFT and direction != 0:
            direction = 2
        elif button == curses.KEY_UP and direction != 1:
            direction = 3

        while food == 0:
            y, x = random.randrange(1, scr_size[0] - 1), random.randrange(1, scr_size[1] - 1)
            if win.inch(y, x) == ord(" "):
                win.addch(y, x, ord("@"))
                food = 1

        win.addch(head[0], head[1], "█")
        if direction == 0:
            head[1] += 1
            time.sleep(0.04)
        elif direction == 1:
            head[0] += 1
            time.sleep(0.07)
        elif direction == 2:
            head[1] -= 1
            time.sleep(0.04)
        elif direction == 3:
            head[0] -= 1
            time.sleep(0.07)

        tail = body[-1][:]
        for b in range(len(body) - 1, 0, -1):
            body[b] = body[b - 1][:]
        body[0] = head[:]
        if win.inch(head[0], head[1]) != ord(" "):
            if win.inch(head[0], head[1]) == ord("@"):
                food = 0
                body.append(body[-1] + body[-2] + body[-3] + body[-4] + body[-5])
                score += 1
            else:
                game_over = 1
        win.refresh()
    '''msg_1 = "GAME OVER"
    msg_2 = "You've made " + str(score) + " points."
    msg_3 = "zero. null. nothing."
    msg_4 = "Loser! "
    msg_5 = "If you want to play again, press SPACE."
    msg_6 = "If you want to quit and run away like coward press Q or ESC."
    win.addstr()'''
game()
curses.endwin()
