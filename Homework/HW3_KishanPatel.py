"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 03 - September 20th, 2019
"""
import time
import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

pen.pu()
pen.goto(-350, 0)
pen.pd()

#Triangle
pen.color("red")
for x in range(3):
    pen.left(360 / 3)
    pen.fd(100)

pen.pu()
pen.fd(150)
pen.pd()

#Square
pen.color("blue")
for x in range(4):
    pen.left(360 / 4)
    pen.fd(100)

pen.pu()
pen.fd(150)
pen.pd()

#Pentagon
pen.color("green")
for x in range(5):
    pen.left(360 / 5)
    pen.fd(100)

pen.pu()
pen.goto(200, 50)
pen.pd()

#Concentric Circles
for radius in range(1, 250, 50):
    pen.right(90)
    pen.fd(radius)
    pen.right(270)
    pen.pd()
    pen.circle(radius)
    pen.pu()
    pen.goto(200, 50)




paper.exitonclick()
time.sleep(6000)