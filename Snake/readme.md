# 1. Autores
1. Juan Pablo Chavez A01721844
2. Bryan Alejandro Cortes A01284228
---
# 2. funciones
1. La comida podrá moverse al azar despues x pasos
```python
if movement == 10:
        food = food - listMoveFood[randrange(0,4)]
        movement = 0
```
2. La comida no deberá de salirse de la ventana 
```python
setup(420, 420, 370, 0)
```
3. Se debe elegir al azar el movimiento de la comida despues de ingerirla
```python
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
```
4. Función para desplegar la información de los integrantes del equipo 
```python
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
```
5. La food debe ser un pequeño circulo
```python
 up()
    goto(food.x + 5, food.y + 5)
    dot(10, colorFood)
```
6. Cada vez que se corra el juego (play) o que el snake consuma la food, la snake y la food deberán asignarles colores diferentes entre sí (no rojo)
 ```python
listOfColors = ['darkcyan', 'blue', 'green', 'yellow', 'purple', 'cyan', 'fuchsia', 'gray', 'lime', 'orange']
colorSnake = listOfColors[randrange(0,9)]
colorFood = listOfColors[randrange(0,9)]

if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        colorSnake = listOfColors[randrange(0,9)]
        colorFood = listOfColors[randrange(0,9)]
    else:
        snake.pop(0)

    clear()
```  
8. Cambiar el nombre de la ventana del videojuego con el nombre del equipo
```python
title("Equipo 6: Bryan Cortés y Juan Pablo Chavez")
```
