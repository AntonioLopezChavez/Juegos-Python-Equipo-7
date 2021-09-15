from random import *
from turtle import *
from typing import Counter
from freegames import path

car = path('car.gif')
rubb = ("python","c++","html","css","java","flutter","c","cpp","py","django","db","cs","code","pro","stress","macos","windows","linux","data","science","msft","google","fb","intern","yahoo","linkedin","binary","sort","merge","bigO","$","bug","python","c++","html","css","java","flutter","c","cpp","py","django","db","cs","code","pro","stress","macos","windows","linux","data","science","msft","google","fb","intern","yahoo","linkedin","binary","sort","merge","bigO","$","bug")
tiles = list(rubb)
state = {'mark': None}
hide = [True] * 64
numero = 0

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
    global numero 
    numero += 1
    print(numero)
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

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
    write(numero, font=20)
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