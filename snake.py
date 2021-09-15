"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

# Snake.py

# Hugo Edgar Palomares - A01741537
# Antonio López Chávez - A01741741
# TC1001S

from random import choice, randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    
    update()
    ontimer(move, 100)
    moveFood()
    

def moveFood():
    randx = randrange(-1, 2) * 10
    randy = randrange(-1, 2) * 10
    if randy == 0:
        food.x = food.x + randx
    else:
        food.y = food.y + randy

colorList = ['blue', 'black', 'green', 'purple', 'orange']
snakeColor = choice(colorList)
foodColor = choice(colorList)
while foodColor == snakeColor:
    snakeColor = choice(colorList)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()

done()