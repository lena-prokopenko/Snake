import curses
import time
import random
screen = curses.initscr()
dims = screen.getmaxyx()
screen.keypad(1)
​
def game(): #the function of the game
    screen.nodelay(1)
    head = [1, 1]
    body = [head[:]]*5
    screen.border()
    direction = 0 #0=right, 1=down, 2=left, 3=up
    gameover = False
    food = False
    deadcell = body[-1][:]
​
    while not gameover:
​
        if deadcell not in body:
            screen.addch(deadcell[0], deadcell[1], ' ')
        screen.addch(head[0], head[1], 'X')
​
        action = screen.getch()
​
        while not food:
            y, x = random.randrange(1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' '):
                food = True
                screen.addch(y, x, ord('@'))
​
​
        if action == curses.KEY_UP and direction != 1:
            direction = 3
        elif action == curses.KEY_DOWN and direction != 3:
            direction = 1
        elif action == curses.KEY_RIGHT and direction != 2:
            direction = 0
        elif action == curses.KEY_LEFT and direction != 0:
            direction = 2
​
        if direction == 0:
            head[1] += 1
        elif direction == 2:
            head[1] -= 1
        elif direction == 1:
            head[0] += 1
        elif direction == 3:
            head[0] -= 1
​
        deadcell = body[-1][:]
        for z in range(len(body)-1, 0, -1):
            body[z] = body[z-1][:]
​
        body[0] = head[:]
​
        if screen.inch(head[0], head[1]) != ord(' '):
            if screen.inch(head[1]) == ord('@'):
                food = False
                body.append(body[-1])
            else:
                gameover = True
        screen.move(dims[0]-1, dims[1]-1)
        screen.refresh()
        time.sleep(0.1)
game()
curses.endwin()
