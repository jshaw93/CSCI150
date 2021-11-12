# James Shaw
# picture.py
# 11/4/21

import turtle
import random

window = turtle.Screen()
bob = turtle.Turtle()
bob.speed(0)


def move_to_when_click(x_coord, y_coord):
    bob.penup()
    bob.setpos(x_coord, y_coord)


def draw_flower_red():
    """
    Produces a 9 petaled red flower
    """
    orientation = random.randint(10, 35)
    bob.setheading(orientation)
    bob.pendown()
    bob.fillcolor("red")
    bob.begin_fill()
    for _ in range(9):
        bob.circle(40, 190)
        bob.setheading(bob.heading()+90)
    bob.end_fill()
    bob.penup()
    bob.setheading(0)


def draw_flower_blue():
    """
    Produces a 9 petaled blue flower
    """
    orientation = random.randint(10, 35)
    bob.setheading(orientation)
    bob.pendown()
    bob.fillcolor("blue")
    bob.begin_fill()
    for _ in range(9):
        bob.circle(40, 190)
        bob.setheading(bob.heading()+90)
    bob.end_fill()
    bob.penup()
    bob.setheading(0)


def draw_flower_green():
    """
    Produces a unique looking green flower with 4 petals
    """
    orientation = random.randint(0, 360)
    bob.setheading(orientation)
    bob.pendown()
    bob.fillcolor("green")
    bob.begin_fill()
    for _ in range(4):
        bob.circle(40, 190)
        bob.setheading(bob.heading()+85)
    bob.end_fill()
    bob.penup()
    bob.setheading(0)


def draw_stem():
    """
    Produces a stem from the position of the turtle, downwards off the screen
    """
    bob.pendown()
    pos_x = bob.pos()[0]
    new_pos = (pos_x, -1400)
    bob.goto(new_pos)
    bob.penup()


def draw_sun():
    """
    Produces a yellow sun without outlines
    """
    bob.pendown()
    bob.pencolor("yellow")
    bob.fillcolor("yellow")
    bob.begin_fill()
    for _ in range(20):
        bob.forward(100)
        bob.left(100)
    bob.pencolor("black")
    bob.end_fill()
    bob.penup()


# Set up events to use for the program
window.onclick(move_to_when_click)
window.onkey(draw_flower_blue, 'F1')
window.onkey(draw_flower_red, 'F2')
window.onkey(draw_flower_green, 'F3')
window.onkey(draw_stem, 't')
window.onkey(draw_sun, 's')

window.listen()
window.mainloop()
