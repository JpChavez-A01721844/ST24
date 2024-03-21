"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

# Overall movement
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
movement = 0

# Colors
listColors = ['darkcyan', 'blue', 'green', 'yellow', 'purple', 'cyan', 'fuchsia', 'gray', 'lime', 'orange']
listMoveFood = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10)]
colorSnake = listColors[randrange(0,9)]
colorFood = listColors[randrange(0,9)]

writer = Turtle()

def maya():
    pass

def info_alumnos():
    color('#F3A1FF')
    maya()
    writer.up()
    writer.goto(-100,190)
    writer.color('blue')
    writer.write('Juan Pablo Chavez A017844',align='left', font=('Arial', 10, 'normal'))
    writer.goto(-100,170)
    writer.color('red')
    writer.write('Bryan Cortés A01248228',align='left',font=('Arial',10,'normal'))
    writer.down()
    writer.hideturtle()

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global colorSnake
    global colorFood
    global movement
    global food
    
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    movement = movement + 1

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if movement == 10:
        food = food - listMoveFood[randrange(0,4)]
        movement = 0

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        colorSnake = listColors[randrange(0,9)]
        colorFood = listColors[randrange(0,9)]
        movement = 0
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    up()
    goto(food.x + 5, food.y + 5)
    dot(10, colorFood)

    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
title("Equipo 6: Bryan Cortés y Juan Pablo Chavez")
info_alumnos()
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()