"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 11 - December 2nd, 2019
"""


class Dog:
    """Declaration of Dog Class"""

    species = "canis familiaris"

    def __init__(self, dogName, dogBreed):
        self.name = dogName
        self.breed = dogBreed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name + " knows " + trick)

    def knows(self, trick):
        if trick in self.tricks:
            print("Yes, " + self.name + " knows " + trick)
            return True
        else:
            print("No, " + self.name + " doesn't know " + trick)
            return False
