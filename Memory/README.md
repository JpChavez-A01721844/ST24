# 1. Autores
1. Juan Pablo Chavez A01721844
2. Bryan Alejandro Cortes A01284228
---
# 2. Funciones
1. Contar y desplegar el numero de taps, añadir un color de fondo de la memorama
- Bryan Alejandro Cortes
```python
taps = 0

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    
    if (x >= -200 and x <= 200) and (y >= -200 and y <= 200):
        taps += 1
        countTabs()

bgcolor('cyan')
```
2. Desplegar los nombres de los integrantes en una parte fuera de la memorama, añadir los nombres en la ventana(title)
- Juan Pablo Chavez
```python
def info_alumnos():
    writer.up()
    writer.goto(-120,250)
    writer.color('blue')
    writer.write('Juan Pablo Chavez A017844', align='left', font=('Arial', 14, 'normal'))
    writer.goto(-120,270)
    writer.color('magenta')
    writer.write('Bryan Cortés A01248228', align='left', font=('Arial', 14, 'normal'))
    writer.down()

title('Memorama - Juan Pablo Chavez y Bryan Cortés')
  ```
3. Detectar si todos los cuadros se han destapado : mostrar un mensaje "Ganaste un auto!!, Felicidades"  y terminar el juego (que no sigan contando los clicks que haga el usuario)
- Juan Pablo Chavez
```python
if hide.count(True) == 0:
        lapiz1.up()
        lapiz1.goto(-150, -300)
        lapiz1.color('Green')
        lapiz1.write('Congratulations!', font = ('Arial', 30, 'normal'))
        lapiz1.down()
        onscreenclick(None)
  ```
4. Utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria o para aprender de algún tópico en particular usando emojis de banderas, o alimentos o animales o…: Poner un color diferente al momento de dibujar los cuadros de la memoria.
- Bryan Alejandro Cortes
```python
emojis = ['\U0001F950', '\U0001F95E', '\U0001F354', '\U0001F355', '\U0001F32D', '\U0001F32F', '\U0001F9C6', '\U0001F37F', 
          '\U0001F371', '\U0001F9C0', '\U0001F357', '\U0001F35F', '\U0001F96A', '\U0001F32E', '\U0001F32F', '\U0001F959',
          '\U0001FAD4', '\U0001F958', '\U0001F372', '\U0001F957', '\U0001F96B', '\U0001F35C', '\U0001F96E', '\U0001F361',
          '\U0001F961', '\U0001F960', '\U0001F95F', '\U0001F364', '\U0001F363', '\U0001F35D', '\U0001F969', '\U0001F96F']
  ```
---
# GIF
![](memory.gif)
