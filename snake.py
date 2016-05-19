import curses
import time
import random
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
game()
curses.endwin()
