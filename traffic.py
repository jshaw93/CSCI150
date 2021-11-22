# James Shaw
# traffic.py
# 11/11/21

import turtle

screen = turtle.Screen()

# Setting up multiple turtles for use in the program loop
bob = turtle.Turtle()
jim = turtle.Turtle()
jill = turtle.Turtle()
light_turtle = turtle.Turtle()
bob.hideturtle()
jim.hideturtle()
jill.hideturtle()
light_turtle.hideturtle()
bob.speed(0)
jim.speed(0)
jill.speed(0)
light_turtle.speed(0)

orig_pos = bob.pos()

bob.penup()
jim.penup()
jill.penup()
light_turtle.penup()

# Positioning turtles to starting positions
y_coord = orig_pos[1]-200
new_pos = (orig_pos[0], y_coord)
bob.goto(new_pos)
jim.goto((new_pos[0], new_pos[1]+120))
jill.goto((new_pos[0], new_pos[1]+240))
light_turtle.goto((new_pos[0], new_pos[1]-10))

is_drawn = False


def draw_light():
    """
    Does nothing if already ran once.
    Produces the original configuration for the traffic light, then starts the state machine.
    """
    global is_drawn
    if is_drawn:
        return
    is_drawn = True
    light_turtle.pendown()
    light_turtle.fillcolor("grey")
    light_turtle.begin_fill()
    light_turtle.forward(60)
    light_turtle.left(90)
    light_turtle.forward(340)
    light_turtle.circle(60, 180)
    light_turtle.setheading(270)
    light_turtle.forward(340)
    light_turtle.left(90)
    light_turtle.forward(60)
    light_turtle.end_fill()

    bob.pendown()
    bob.fillcolor("black")
    bob.begin_fill()
    bob.circle(50)
    bob.end_fill()

    jim.pendown()
    jim.fillcolor("black")
    jim.begin_fill()
    jim.circle(50)
    jim.end_fill()

    jill.pendown()
    jill.fillcolor("black")
    jill.begin_fill()
    jill.circle(50)
    jill.end_fill()

    # Begins the state machine loop
    state_machine()


state = 2


def state_machine():
    """
    Begins cycling through states 0-2 to determine lighting, switching unused lights to black, then continuing.
    """
    global state
    if state == 0:
        bob.fillcolor("black")
        bob.begin_fill()
        bob.circle(50)
        bob.end_fill()
        jim.fillcolor("yellow")
        jim.begin_fill()
        jim.circle(50)
        jim.end_fill()
        state = 1
        screen.ontimer(state_machine, 2000)
    elif state == 1:
        jim.fillcolor("black")
        jim.begin_fill()
        jim.circle(50)
        jim.end_fill()
        jill.fillcolor("red")
        jill.begin_fill()
        jill.circle(50)
        jill.end_fill()
        state = 2
        screen.ontimer(state_machine, 5000)
    else:
        jill.fillcolor("black")
        jill.begin_fill()
        jill.circle(50)
        jill.end_fill()
        bob.fillcolor("green")
        bob.begin_fill()
        bob.circle(50)
        bob.end_fill()
        state = 0
        screen.ontimer(state_machine, 5000)


screen.onkey(draw_light, "space")

screen.listen()
screen.mainloop()
