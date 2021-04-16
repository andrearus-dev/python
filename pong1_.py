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
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # turtles usually draw a line as they're moving but we don't want that
paddle_a.goto(-350, 0)

# Paddle B

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # turtles usually draw a line as they're moving but we don't want that
paddle_a.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)

# Function


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# Main game loop
while True:
    window.update()
