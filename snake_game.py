# Building snake game
from turtle import *
from random import randrange
from freegames import square.vector

# Variables - food, snake and aim

food = vector(0, 0)
snake = vector(10, 0)
aim = vector(0, -10)

# 3 Functions - Change, Inside and Move
