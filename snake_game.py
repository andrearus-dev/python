# Building snake game
from turtle import *
from random import randrange
from freegames import square, vector

# Variables - food, snake and aim

food = vector(0, 0)
snake = vector(10, 0)
aim = vector(0, -10)

# 3 Functions - Change, Inside and Move


def change(x, y):
    aim.x = x
    aim.y = y


def inside(head):
    # boundaries values - when the snake crosses that boundary the game is over
    return -200 < head.x < 190 and -200 < head.y < 190


def moves():
    head = snake[-1].copy()
    head.move(aim)
