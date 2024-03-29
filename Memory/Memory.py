"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

emojis = ['\U0001F950', '\U0001F95E', '\U0001F354', '\U0001F355', '\U0001F32D', '\U0001F32F', '\U0001F9C6', '\U0001F37F', 
          '\U0001F371', '\U0001F9C0', '\U0001F357', '\U0001F35F', '\U0001F96A', '\U0001F32E', '\U0001F32F', '\U0001F959',
          '\U0001FAD4', '\U0001F958', '\U0001F372', '\U0001F957', '\U0001F96B', '\U0001F35C', '\U0001F96E', '\U0001F361',
          '\U0001F961', '\U0001F960', '\U0001F95F', '\U0001F364', '\U0001F363', '\U0001F35D', '\U0001F969', '\U0001F96F']
car = path('car.gif')
tiles = emojis * 2
state = {'mark': None}
hide = [True] * 64
taps = 0

lapiz1 = Turtle(visible = False)
writer = Turtle(visible = False)

def info_alumnos():
    writer.up()
    writer.goto(-120,250)
    writer.color('blue')
    writer.write('Juan Pablo Chavez A017844', align='left', font=('Arial', 14, 'normal'))
    writer.goto(-120,270)
    writer.color('magenta')
    writer.write('Bryan Cortés A01248228', align='left', font=('Arial', 14, 'normal'))
    writer.down()

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'lime')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    
    if (x >= -200 and x <= 200) and (y >= -200 and y <= 200):
        taps += 1
        countTabs()
        spot = index(x, y)
        mark = state['mark']
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

def countTabs():
    lapiz1.clear()
    lapiz1.up()
    lapiz1.goto(-50,-250)
    lapiz1.color('blue')
    lapiz1.write(f"Taps: {taps}", font = ('Arial', 30, 'normal'))
    lapiz1.down()

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()

    if hide.count(True) == 0:
        lapiz1.up()
        lapiz1.goto(-150, -300)
        lapiz1.color('Green')
        lapiz1.write('Congratulations!', font = ('Arial', 30, 'normal'))
        lapiz1.down()
        onscreenclick(None)

    ontimer(draw, 100)


#shuffle(tiles)
setup(620, 620, 370, 0)
bgcolor('cyan')
title('Memorama - Juan Pablo Chavez y Bryan Cortés')
info_alumnos()
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
