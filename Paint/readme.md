# 1. Autores
1. Juan Pablo Chavez A01721844
2. Bryan Alejandro Cortes A01284228

# 2. Funciones
---
**1. Un color nuevo**
- Juan Pablo Chavez
```python
  onkey(lambda: color('orange'), 'O')
```
**2. Dibujar un círculo**
- Bryan Alejandro Cortes
```python
def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(20):
        forward(end.x - start.x)
        left(18)
    end_fill()
```
**3. Desplegar los 3 o 4 nombres de los integrantes del equipo, añadiendo la siguiente función**
- Bryan Alejandro Cortes
```python
 def info_alumnos():
  writer.up()
  writer.goto(0,190)
  writer.color('blue')
  writer.write('Juan Pablo Chavez A017844',align='left', font=('Arial', 10, 'normal'))
  writer.goto(0,170)
  writer.color('black')
  writer.write('Bryan Cortés A01248228',align='left',font=('Arial',10,'normal'))
  writer.goto(0,150)
  writer.color('green')
  writer.write('NameApellidoPaternoMaternoMatricula',align='left',font=('Arial',10,'normal'))
```
**4. Completar el rectángulo**
- Juan Pablo Chavez
```python
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()
```
**5. Completar el triángulo**
- Bryan Alejandro Cortes
```python
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for _ in range(3):
        goto(end.x, end.y)
        goto(start.x, start.y)
        right(120)
    end_fill()
```
---
6. Modificar el README con la siguiente información :
  - código(md) de las funciones que se añadieron
  - indicando con un titulo el autor
  - Añadir un gif del funcionamiento del videojuego.

# GIF
