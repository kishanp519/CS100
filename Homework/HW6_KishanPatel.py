"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 06 - October 8th, 2019
"""


def hasFinalLetter(strList, letters):
    validString = []
    for str in strList:
        for letter in  letters:
            if str[-1] == letter:
                validString.append(str)
    return validString


def isDivisible(maxInt, twoInts):
    divisibleNumbers = []
    for number in range(1, maxInt):
        if number % twoInts[0] == 0 and number % twoInts[1] == 0:
            divisibleNumbers.append(number)
    return divisibleNumbers


# 1B) Test Case #1
strList = ["Hi", "my", "name", "is", "Kishan", "Patel"]
letters = ["y", "e", "n"]
print("1B) Test Case #1 Result:", hasFinalLetter(strList, letters))

# 1B) Test Case #2
strList = ["This", "will", "be", "returning", "an", "empty", "LIST"]
letters = ["a", "c", "q", "G", "b", "L"]
print("1B) Test Case #2 Result:", hasFinalLetter(strList, letters))

# 1B) Test Case #3
strList = ["THIS", "list", "IS", "a", "MIXTURE", "of", "UPPERCASE", "and", "LOWERCASE", "letters"]
letters = ["t", "f", "E", "d"]
print("1B) Test Case #3 Result:", hasFinalLetter(strList, letters))

print("")

# 2B) Test Case #1
maxInt = 100
twoInts = (2, 5)
print("2B) Test Case #1 Result:", isDivisible(maxInt, twoInts))

# 2B) Test Case #2
maxInt = 18
twoInts = (9, 2)
print("2B) Test Case #2 Result:", isDivisible(maxInt, twoInts))

# 2B) Test Case #3
maxInt = 80
twoInts = (3, 7)
print("2B) Test Case #3 Result:", isDivisible(maxInt, twoInts))
