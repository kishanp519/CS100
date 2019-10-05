"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 10 - October 3rd, 2019
"""

def totalAs(scoresList):
    counter = 0
    for score in scoresList:
        if score >= 90:
            counter += 1
    return counter

def findEvens(integerList):
    evens = []
    for integer in integerList:
        if integer % 2 == 0:
            evens.append(integer)
    return evens

def testReturn(sequence):
    for i in sequence:
        return i

def hasEven(integerList):
    for integer in integerList:
        if integer % 2 == 0:
            return True
    return False

def getDivergent(words):
    counter = 0
    for word in words:
        if word[0] == word[-1]:
            counter += 1
    return [counter, len(words) - counter]



print(totalAs([89, 95, 23, 100]))
print(findEvens([17, 8, 9, 13, 2]))
print(testReturn("hello"))
print(hasEven([17, 8, 9, 13, 2]))

advice = ['the', 'secret', 'to', 'a', 'better', 'health', 'is', 'exercise']
print(getDivergent(advice))
