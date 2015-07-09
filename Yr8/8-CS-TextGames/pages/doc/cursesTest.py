import curses
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.addstr('This is a string')

def drawSpaceship(line,column):
    '''draw a spaceship to a given line and column'''
    #spaceship is a string literal
    spaceship=r''' ^
/ \
| |'''
    ##iterate over the spaceship string, and print to each line
    for y, row in enumerate(spaceship.splitlines(), 2):
        screen.addstr(y+line, column, row)

def moveShip(position,distance):
    newPos = position+distance
    ##draw spaceship at bottom of screen with horizontal position
    drawSpaceship(curses.LINES-5,newPos)
    return newPos

def drawbullet(line,column):
    if line == 1:
        return False
    else:
        screen.addstr(line,column,'^')
        return True



position = int((curses.COLS-1)/2)
shootbullet = False
while True:
    event = screen.getch()
    if event == ord("q"): break
    elif event == ord("a"):
        screen.clear()
        position = moveShip(position,1)
    elif event == ord("d"):
        screen.clear()
        position = moveShip(position,-1)
    elif event == ord("w"):
        screen.clear()
        drawSpaceship(curses.LINES-5,position)
        shootbullet = True
        line = curses.LINES-6
        bulletPos = position
    elif event == ord(" "):
        screen.clear()
        screen.addstr("The User Pressed The Space Bar")
    if shootbullet == True:
        shootbullet = drawbullet(line,bulletPos)
        line-=1
    screen.refresh()
