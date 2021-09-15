# Memory.py

# Hugo Edgar Palomares - A01741537
# Antonio López Chávez - A01741741
# Carlos Seda - A00827514
# TC1001S

from random import *
from turtle import *
from typing import Counter
from freegames import path

car = path('car.gif')
rubb = ("python","c++","html","css","java","flutter","c","cpp","py","django","db","cs","code","pro","stress","macos","windows","linux","data","science","msft","google","fb","intern","yahoo","linkedin","binary","sort","merge","bigO","$","bug","python","c++","html","css","java","flutter","c","cpp","py","django","db","cs","code","pro","stress","macos","windows","linux","data","science","msft","google","fb","intern","yahoo","linkedin","binary","sort","merge","bigO","$","bug")
tiles = list(rubb)
state = {'mark': None}
hide = [True] * 64
nClicks = 0
pares = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global nClicks 
    global pares
    nClicks += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        pares += 1


def draw():
    "Draw image and tiles."
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
        goto(x + 25, y+18) #########
        color('black')
        write(tiles[mark], font=('Arial', 10, 'normal'), align='center')

    penup()
    goto(-200,200)
    write(nClicks, font=20)
    if pares == 32:
        goto(-100,200)
        write("JUEGO COMPLETADO", font=20)

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 450, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

