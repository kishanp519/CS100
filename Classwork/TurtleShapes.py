"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 5 - September 17th, 2019
"""

import time
import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

sides = int(input("Enter the amount of sides: "))
sideLength = int(input("Enter the length of one side: "))
gap = int(input("Enter the gap between each shape: "))

pen.color("red")
for x in range(sides):
    pen.fd(sideLength)
    pen.right(360 / sides)

pen.pu()
pen.fd(sideLength + gap)
pen.pd()

pen.color("blue")
for x in range(sides):
    pen.fd(sideLength)
    pen.right(360 / sides)

pen.pu()
pen.fd(sideLength + gap)
pen.pd()

pen.color("green")
for x in range(sides):
    pen.fd(sideLength)
    pen.right(360 / sides)

paper.exitonclick()
time.sleep(6000)
