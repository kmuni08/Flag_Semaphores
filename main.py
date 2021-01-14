from turtle import *
from shapes import *
from time import sleep

semaphore = {
    "A": (225, -90),
    "1": (225, -90),
    "B": (180, -90),
    "2": (180, -90),
    "C": (135, -90),
    "3": (135, -90),
    "D": (90, -90),
    "4": (90, -90),
    "E": (-90, 45),
    "5": (-90, 45),
    "F": (-90, 0),
    "6": (-90, 0),
    "G": (-90, -45),
    "7": (-90, -45),
    "H": (180, 225),
    "8": (180, 225),
    "I": (135, 225),
    "9": (135, 225),
    "J": (90, 0),
    "K": (225, 90),
    "0": (225, 90),
    "L": (225, 45),
    "M": (225, 0),
    "N": (225, -45),
    "O": (180, -135),
    "P": (180, 90),
    "Q": (180, 45),
    "R": (180, 0),
    "S": (180, -45),
    "T": (135, 90),
    "U": (135, 45),
    "V": (90, -45),
    "W": (45, 0),
    "X": (45, -45),
    "Y": (135, 0),
    "Z": (0, -45),
    " ": (-90, -90)
}

semaphore_phrases = {
    "ERROR": ((135, 45), (225, -45)),
    "CANCEL": (135, -45),
    "NUMERALS": (90, 45),
    "LETTERS": (90, 0)
}

myPen = Turtle()
window = turtle.Screen()
window.bgcolor("white")
draw_signalman(myPen)

message = "1A2B"

if message != "ERROR" and message != "CANCEL" and message != "NUMERALS":
    for letter in message:
        turtle.clear()
        # Draw First Flag
        angle = semaphore[letter][0]
        if angle >= 90:
            leftArm(turtle, angle)
        else:
            rightArm(turtle, angle)

        # Draw Second Flag
        angle = semaphore[letter][1]
        if angle > 90:
            leftArm(turtle, angle)
        else:
            rightArm(turtle, angle)

        myPen.getscreen().update()
        sleep(1)


def draw_flag_error(key):
    for i in range(2):
        turtle.clear()
        angle = semaphore_phrases[key][i][0]
        if angle >= 90:
            leftArm(turtle, angle)
        else:
            rightArm(turtle, angle)

        # Draw Second Flag
        angle = semaphore_phrases[key][i][1]
        if angle > 90:
            leftArm(turtle, angle)
        else:
            rightArm(turtle, angle)

        myPen.getscreen().update()
        sleep(0.3)


def draw_flag(key):
    turtle.clear()
    angle = semaphore_phrases[key][0]
    print("first ", angle)
    if angle >= 90:
        leftArm(turtle, angle)
    else:
        rightArm(turtle, angle)

    # Draw Second Flag
    angle = semaphore_phrases[key][1]
    print("second ", angle)
    if angle > 90:
        leftArm(turtle, angle)
    else:
        rightArm(turtle, angle)

    myPen.getscreen().update()
    sleep(0.3)


if message == "ERROR" or message == "CANCEL" or message == "NUMERALS":
    for key in semaphore_phrases:
        if message == "ERROR" and key == "ERROR":
            draw_flag_error(key),
            draw_flag_error(key)
        elif message == "CANCEL" and key == "CANCEL":
            draw_flag(key),
        elif message == "NUMERALS" and key == "NUMERALS":
            draw_flag(key)
