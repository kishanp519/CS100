"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 03 - September 20th, 2019
"""

import math
import time
import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

pen.pu()
pen.goto(-350, 0)
pen.pd()

# Shapes
pen.color("red")
for sideLength in range(3, 6):
    if sideLength == 4:
        pen.color("blue")
    if sideLength == 5:
        pen.color("green")
    for length in range(sideLength):
        pen.left(360 / sideLength)
        pen.fd(100)
    if sideLength < 5:
        pen.pu()
        pen.fd(150)
        pen.pd()

pen.pu()
pen.goto(200, 50)
pen.pd()

# Concentric Circles
pen.color("black")
for radius in range(0, 250, 50):
    pen.right(90)
    pen.fd(radius)
    pen.right(270)
    pen.pd()
    pen.circle(radius)
    pen.pu()
    pen.goto(200, 50)

# Math Operations
factorial = math.factorial(100)
logValue = math.log(1000000, 2)
greatestDivisor = math.gcd(63, 49)

print("100!:", factorial)
print("log(1000000):", logValue)
print("Greatest Common Divisor of 63 and 49:", greatestDivisor)

paper.exitonclick()
time.sleep(6000)
