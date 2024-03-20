"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector

def info_alumnos():
  writer.up()
  writer.goto(0,190)
  writer.color('blue')
  writer.write('Name Apellido Paterno Materno Matricula',align='left', font=('Arial', 10, 'normal'))
  writer.goto(0,170)
  writer.color('pink')
  writer.write('NameApellidoPaternoMaternoMatricula',align='left',font=('Arial',10,'normal'))
                                                                                
def line(start, end):
    """Draw line from start to end.
    start - vector (x,y)
    end - vector (x,y)
    uo() - levanta pluma
    down() - baja pluma"""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.x - (start.x)*2 )
        left(90)


    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key. Solo se llama cujando se va a modificar el shape"""
    state[key] = value

# estado inicial del paint - diccionario - start - si el usuario ya dio un click mouse- shape - linea
state = {'start': None, 'shape': line}
# setup(ancho,alto, x_esq, suo, izq_wind, y_Esq.sup, izq_wind)
setup(420, 420, 370, 0)
# registra la funcion que atendera los eventos del mouse
onscreenclick(tap)
listen()
onkey(undo, 'u') # funcion/tecla
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('#33FF4F'), 'Z')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
