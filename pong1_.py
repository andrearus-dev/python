# Pong game for beginners
# Getting started

import turtle

window = turtle.Screen()
window.title("Pong by @TokyoEdTech")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()  # turtles usually draw a line as they're moving but we don't want that
paddle_a.goto(-350, 0)


# Main game loop

while True:
    window.update()
