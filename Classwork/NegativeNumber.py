"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture # - October 17th, 2019
"""

def getNegativeNumber():
    value = 0
    while value >= 0:
        value = int(input("Enter a number (negative to exit loop): "))
    return value


print("Negative Value Entered:", getNegativeNumber())