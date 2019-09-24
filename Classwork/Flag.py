"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 7 - September 24th, 2019
"""

import time
import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

length = 45
sides = 3
amount = 4


def draw_flag(pen, sides, length):
    for x in range(sides):
        pen.fd(length)
        pen.rt(360 / sides)


def flag_lines(pen, sides, length, amount):
    for i in range(amount):
        draw_flag(pen, sides, length)
        pen.pu()
        pen.fd(length)
        pen.pd()



flag_lines(pen, sides, length, amount)
pen.setheading(90)
flag_lines(pen, sides, length, amount)
pen.setheading(180)
flag_lines(pen, sides, length, amount)
pen.setheading(270)
flag_lines(pen, sides, length, amount)

paper.exitonclick()
time.sleep(6000)
