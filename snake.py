import curses
import time
import random
<<<<<<< HEAD

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

    msg_1 = "GAME OVER"
    msg_2 = "You've made " + str(score) + " points."
    msg_3 = "zero. null. nothing."
    msg_4 = "Loser! "
    msg_5 = "If you want to play again, press SPACE."
    msg_6 = "If you want to quit and run away like coward just press Q or ESC."
    win.clear()
    win.nodelay(0)
    win.addstr(scr_size[0] // 2 - 3, scr_size[1] // 2 - len(msg_1) // 2, msg_1, curses.A_UNDERLINE | curses.A_BOLD | curses.A_STANDOUT)
    win.addstr(scr_size[0] // 2 - 2, scr_size[1] // 2 - len(msg_2) // 2, msg_2, curses.A_UNDERLINE | curses.A_BOLD | curses.A_STANDOUT)
    if score == 0:
        win.addstr(scr_size[0] // 2 - 1, scr_size[1] // 2 - len(msg_3) // 2, msg_3, curses.A_UNDERLINE | curses.A_BOLD | curses.A_STANDOUT)
    else:
        win.addstr(scr_size[0] // 2, scr_size[1] // 2 - len(msg_4) // 2, msg_4, curses.A_UNDERLINE | curses.A_BOLD | curses.A_STANDOUT)
    win.addstr(scr_size[0] // 2 + 1, scr_size[1] // 2 - len(msg_5) // 2, msg_5, curses.A_UNDERLINE | curses.A_BOLD | curses.A_STANDOUT)
    win.addstr(scr_size[0] // 2 + 2, scr_size[1] // 2 - len(msg_6) // 2, msg_6, curses.A_UNDERLINE | curses.A_BOLD | curses.A_STANDOUT)
    win.refresh()
    button = 0
    while button not in [27, 113, 32]:
        button = win.getch()
    if button == 32:
        win.clear()
        game()
=======
screen = curses.initscr()
curses.curs_set(0)
dims = screen.getmaxyx()
screen.keypad(1)

def game(): #the function of the game
    screen.nodelay(1)
    head = [1, 1]
    body = [head[:]]*5
    screen.border()
    direction = 0 #0=right, 1=down, 2=left, 3=up
    gameover = False
    food = False
    deadcell = body[-1][:]

    while not gameover:

        if deadcell not in body:
            screen.addch(deadcell[0], deadcell[1], ' ')
        screen.addch(head[0], head[1], 'X')

        action = screen.getch()

        while not food:
            y, x = random.randrange(1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' '):
                food = True
                screen.addch(y, x, ord('@'))

        if action == curses.KEY_UP and direction != 1:
            direction = 3
        elif action == curses.KEY_DOWN and direction != 3:
            direction = 1
        elif action == curses.KEY_RIGHT and direction != 2:
            direction = 0
        elif action == curses.KEY_LEFT and direction != 0:
            direction = 2

        if direction == 0:
            head[1] += 1
        elif direction == 2:
            head[1] -= 1
        elif direction == 1:
            head[0] += 1
        elif direction == 3:
            head[0] -= 1

        deadcell = body[-1][:]
        for z in range(len(body)-1, 0, -1):
            body[z] = body[z-1][:]

        body[0] = head[:]
        if screen.inch(head[0], head[1]) != ord(' '):
            if screen.inch(head[0], head[1]) == ord('@'):

                food = False
                body.append(body[-1])
            else:
                gameover = True
        screen.move(dims[0]-1, dims[1]-1)
        screen.refresh()
        time.sleep(0.1)
    screen.clear()
    screen.nodelay(0)
    '''message1 = "Game Over"
    message2 = "You have" + str(len(body)-5) + "points"
    message3 = "press Space to play again"
    message4 = "Press Enter to quit"
    screen.addstr(dims[0]/2-1, (dims[1]-len(message1))/2, message1)
    screen.addstr(dims[0]/2, (dims[1]-len(message2))/2, message2)
    screen.addstr(dims[0]/2+1, (dims[1]-len(message3))/2, message3)
    screen.addstr(dims[0]/2+2, (dims[1]-len(message4))/2, message4)
    screen.refresh()
    q = 0
    while q not in [32, 10]:
        g = screen.getch()
    if q == 32:
        game()
    screen.getch()'''
>>>>>>> 7cd5d357ae30337f1fe3a7ba00caa0706ce4d557
game()
curses.endwin()
