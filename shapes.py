import turtle
import math

def createCircle(turtle, color, x, y, radius):
    turtle.speed(0)
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def createRectangle(turtle, color, x, y, width, height):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)
    turtle.getscreen().update()


def draw_rectangular_arm(turtle, color, width, height):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.getscreen().update()

def draw_yellow(heading, x, y):
    # Draw Flag (Yellow section)
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.right(90)
    turtle.fillcolor("#FFFF00")
    turtle.begin_fill()
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.goto(x, y)
    turtle.end_fill()


def draw_red(heading, x, y):
    # Draw Flag (Red section)
    turtle.fillcolor("#FF0000")
    turtle.begin_fill()
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.goto(x, y)
    turtle.end_fill()



def rightArm(turtle, angle):
    turtle.speed(0)
    turtle.penup()
    # Draw Arm
    turtle.goto(10, -10)
    turtle.setheading(angle)
    draw_rectangular_arm(turtle, "black", 60, 10)

    # Draw Stick
    turtle.forward(65)
    turtle.left(90)
    turtle.forward(3)
    turtle.right(90)
    draw_rectangular_arm(turtle, "black", 80, 4)
    turtle.forward(20)
    (x, y) = turtle.position()
    heading = turtle.heading()

    draw_red(heading, x, y)
    draw_yellow(heading, x, y)


def leftArm(turtle, angle):
    turtle.speed(0)
    turtle.penup()
    # Draw Arm
    turtle.goto(-10, 0)
    turtle.setheading(angle)
    draw_rectangular_arm(turtle, "black", 60, 10)
    # Draw Stick
    turtle.forward(65)
    turtle.left(90)
    turtle.forward(3)
    turtle.right(90)
    draw_rectangular_arm(turtle, "black", 80, 4)
    turtle.left(90)
    turtle.forward(3)
    turtle.right(90)

    turtle.forward(20)
    (x, y) = turtle.position()
    heading = turtle.heading()

    draw_red(heading, x, y)
    draw_yellow(heading, x, y)


def draw_signalman(turtle1):
    turtle1.setheading(0)
    createRectangle(turtle1, "black", -20, -150, 40, 150)
    createRectangle(turtle1, "white", -1, -150, 2, 60)
    createCircle(turtle1, "black", 0, 10, 16)
