# James Shaw
# mosaic.py
# 10/25/21

import turtle
import random

window = turtle.Screen()
mine_turtle = turtle.Turtle()  # Hello!

# Code block to populate a list of 16 random colors using hexadecimal color codes.
hex_choices = list("1234567890ABCDEF")
rand_color = ["" for _ in range(16)]  # List comprehension that produces 16 empty string objects within the list variable rand_color
for index in range(len(rand_color)):
    for _ in range(6):
        rand_color[index] += random.choice(hex_choices)  # Concatenating strings in the list with random characters

x = -280
y = 280
orig_pos = (x, y)
mine_turtle.penup()
mine_turtle.pensize(3)
mine_turtle.goto(orig_pos)
mine_turtle.pendown()

for _ in range(4):
    for _ in range(4):
        pos = mine_turtle.pos()
        mine_turtle.pendown()
        mine_turtle.fillcolor("#"+random.choice(rand_color))
        mine_turtle.begin_fill()
        mine_turtle.right(45)

        # Octagon
        for _ in range(8):
            mine_turtle.forward(50)
            mine_turtle.right(45)
        mine_turtle.end_fill()
        mine_turtle.left(45)
        mine_turtle.penup()

        # Circle within octagon
        x_coord_current = pos[0]
        y_coord_current = pos[1]
        mine_turtle.goto(x_coord_current-25, y_coord_current-87.5)
        mine_turtle.pendown()
        mine_turtle.fillcolor("#"+random.choice(rand_color))
        mine_turtle.begin_fill()
        mine_turtle.circle(25)
        mine_turtle.end_fill()
        mine_turtle.penup()

        # Prepare for next shape
        mine_turtle.goto(pos)
        mine_turtle.forward(125)

    # Prepare next line
    y -= 125
    new_pos = (x, y)
    mine_turtle.penup()
    mine_turtle.goto(new_pos)

window.exitonclick()
