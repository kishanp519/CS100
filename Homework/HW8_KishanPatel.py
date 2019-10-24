"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 08 - October 24th, 2019
"""

import random


def twoWords(length, firstLetter):
    lengthWord = ""
    userMessage = "Enter a " + str(length) + "-letter word please: "
    while True:
        lengthWord = input(userMessage)
        if len(lengthWord) == length:
            break

    letterWord = ""
    userMessage = "Enter a word beginning with " + firstLetter + " please: "
    while True:
        letterWord = input(userMessage)
        if letterWord[0].lower() == firstLetter.lower():
            break

    return [lengthWord, letterWord]


def twoWordsV2(length, firstLetter):
    lengthWord = ""
    userMessage = "Enter a " + str(length) + "-letter word please: "
    while len(lengthWord) != length:
        lengthWord = input(userMessage)

    letterWord = ""
    userMessage = "Enter a word beginning with " + firstLetter + " please: "
    letterWord = input(userMessage)
    while letterWord[0].lower() != firstLetter.lower():
        letterWord = input(userMessage)

    return [lengthWord, letterWord]


def enterNewPassword():
    validPassword = False
    while not validPassword:
        password = input("Enter Password: ")
        validLength = False
        hasDigit = False
        if 8 <= len(password) <= 15:
            validLength = True

        if any(char.isdigit() for char in password):
            hasDigit = True

        if validLength and hasDigit:
            validPassword = True

        if not validLength and not hasDigit:
            print("You must enter a password with 8-15 characters and a digit.")
        elif not validLength:
            print("You must enter a password with 8-15 characters.")
        elif not hasDigit:
            print("You must enter a password with a digit.")

    print("Correct Password: ", password)


# print("Problem 1: ", twoWords(4, 'B'))
print("")
# print("Problem 2: ", twoWordsV2(4, 'B'))
print("")
print("Problem 3: (below)")
# enterNewPassword()

print("Problem 4:")
print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
attempts = 0
guessedValue = False
value = random.randint(0, 50)
while not guessedValue and attempts != 5:
    attempts += 1
    guessed = int(input("Guess " + str(attempts) + "? "))
    if guessed == value:
        print("You are right! I was thinking of " + str(value) + "!")
        guessedValue = True
    elif guessed > value:
        print(str(guessed) + " is too high")
    else:
        print(str(guessed) + " is too low")
if not guessedValue and attempts == 5:
    print("The value I was thinking of was " + str(value) + ".")

