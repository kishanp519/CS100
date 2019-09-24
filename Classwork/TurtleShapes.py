"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 5 & 6 - September 17th/19th, 2019
"""

import time
import turtle

paper = turtle.Screen()
pen = turtle.Turtle()



def draw_shape(pen, sides, sideLength, increment, gap, amount):
    for i in range(amount):
        for x in range(sides):
            pen.fd(sideLength + increment)
            pen.rt(360 / sides)
        sideLength = sideLength + increment
       # pen.pu()
       # pen.fd(sideLength + gap)
       # pen.pd()


sides = int(input("Enter the amount of sides: "))
sideLength = int(input("Enter the length of one side: "))
increment = int(input("Enter the amount to increment each side: "))
amount = int(input("Enter the amount of shapes: "))
gap = 0

if amount > 1:
    gap = int(input("Enter the gap between each shape: "))

pen.color("red")
draw_shape(pen, sides, sideLength, increment, gap, amount)

paper.exitonclick()
time.sleep(6000)

