import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


# two objects
# first class

class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

# second class


class snake(object):
    def _init_(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    pass


def redrawWindow(surface):
    drawGrid()
    pygame.display.update()
    pass


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((250, 0, 0), (10, 10))  # colour and position
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
    pass
