# 1. Autores
1. Juan Pablo Chavez A01721844
2. Bryan Alejandro Cortes A01284228

# 2. Funciones
---
**1. Un color nuevo**
**2. Dibujar un círculo**
**3. Desplegar los 3 o 4 nombres de los integrantes del equipo, añadiendo la siguiente función**
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
- Juan Pablo Chavez
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

6. Modificar el README con la siguiente información :
  - código(md) de las funciones que se añadieron
  - indicando con un titulo el autor
  - Añadir un gift del funcionamiento del videojuego.

