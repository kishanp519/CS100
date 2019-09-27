"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 04 - October 1st, 2019
"""
import math
import time
import turtle

paper = turtle.Screen()
pen = turtle.Turtle()


def draw_shape(pen, color, width, length, shape):
    sides = 0
    if shape == "line":
        sides = 1
    elif shape == "triangle":
        sides = 3
    elif shape == "square":
        sides = 4

    pen.color(color)
    pen.pensize(width)
    for x in range(sides):
        pen.fd(length)
        pen.rt(360 / sides)


a = 3
b = 4
c = 5

if a < b:
    print("a < b: OK")
else:
    print("a < b: NOT OK")

if c < b:
    print("c < b: OK")
else:
    print("c < b: NOT OK")

if a + b == c:
    print("a + b = c: OK")
else:
    print("a + b = c: NOT OK")

if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
    print("a^2 + b^2 = c^2: OK")
else:
    print("a^2 + b^2 = c^2: NOT OK")

print("")

possibleShapes = ["line", "triangle", "square"]

validShape = False
while not validShape:
    shape = input("What shape would you like to draw?: ")

    for each in possibleShapes:
        if each == shape:
            validShape = True
            break

    if not validShape:
        print("You have entered an invalid shape name.")
        print("Possible valid shape names: ", possibleShapes)
        continue

validColor = False
while not validColor:
    color = input("What color would you like the shape to be?: ")

    try:
        pen.color(color)

        if pen.pencolor() == color:
            validColor = True
    except:
        print("You have entered an invalid color.")

width = int(input("What is the width each side?: "))
length = int(input("What is the length of each side?: "))

draw_shape(pen, color, width, length, shape)

paper.exitonclick()
time.sleep(6000)
