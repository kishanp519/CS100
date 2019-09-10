"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 2 & 3 - September 5th/10th, 2019
"""

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
age = int(input("Please enter your age: "))

firstInitials = first[0] + first[-1]
lastInitials = last[0] + last[-1]
futureAge = first + " " + last + ", in 10 years you will be " + str(age + 10) + " years old."

print("")
print("Your first and last letters of your full name are:", firstInitials + lastInitials)
print(futureAge)
