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
    body = []
    turns = {}

    def _init_(self, color, pos):
        self.color = color
        self.head = cube(pos)  # cube at the gives position
        self.body.append(self.head)
        self.dirnx = 0  # direction for x
        self.dirny = 1  # both keep track what direction we're moving in

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0),
                         (x, w))  # start and end position
        # going to draw lines every for loop
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
    pass


def redrawWindow(surface):
    global rows, width
    surface.fill(0, 0, 0)
    drawGrid(width, row, surface)
    pygame.display.update()
    pass


def randomSnack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((250, 0, 0), (10, 10))  # colour and position
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)  # speed
        redrawWindow(win)
    pass
