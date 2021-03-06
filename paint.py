# Paint.py

# Hugo Edgar Palomares - A01741537
# Antonio López Chávez - A01741741
# TC1001S

from turtle import *

from freegames import vector


def line(start, end): # Función para crear una linea
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end): # Función para crear un cuadrado
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end): # Función para crear un círculo, completado por alumnos
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    

    for count in range(36):
        forward((end.x - start.x)/10)
        left(10)
        begin_fill()

    end_fill()


def rectangle(start, end): # Función para crear un rectángulo, completado por alumnos
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):

        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x)/2)
        left(90)

    end_fill()


def triangle(start, end): # Función para crear un triángulo, completado por alumnos
    "Draw triangle from start to end." 
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y): # Función para establecer inputs de mouse para iniciar figuras o lineas
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):  # Función para guardar valor de inputs para cambiar figuras y/o colores
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')  # Opciones para seleccionar figuras y colores
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O') # Añadido por alumnos
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()