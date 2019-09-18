"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 5 - September 17th, 2019
"""

import turtle
import time

paper = turtle.Screen()
pen = turtle.Turtle()

pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)

pen.color("red")
pen.width(5)

pen.left(30)
pen.forward(150)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(150)
pen.left(90)

pen.penup()
pen.goto(-20, -40)
pen.pendown()
pen.color("blue")

pen.setheading(0)
pen.forward(75)
pen.left(90)
pen.forward(75)
pen.left(90)
pen.forward(75)
pen.left(90)
pen.forward(75)
pen.left(90)

paper.exitonclick()
time.sleep(6000)
