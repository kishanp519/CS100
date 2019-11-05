"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 10 - November 2nd, 2019
"""


def initialLetterCount(wordList):
    initialCount = {}
    for word in wordList:
        firstLeter = word[0]
        if firstLeter in initialCount:
            initialCount[firstLeter] += 1
        else:
            initialCount[firstLeter] = 1
    return initialCount


def initialLetters(wordList):
    initialWords = {}
    for word in wordList:
        firstLeter = word[0]
        if firstLeter not in initialWords:
            initialWords[firstLeter] = [word]
        elif word not in initialWords[firstLeter]:
            initialWords[firstLeter].append(word)
    return initialWords


def shareALetter(wordList):
    sharesLetters = {}
    for word in wordList:
        sharedWords = []
        for iteratingWord in wordList:
            for x in range(len(word)):
                if word[x] in iteratingWord and iteratingWord not in sharedWords:
                    sharedWords.append(iteratingWord)
        sharesLetters[word] = sharedWords
    return sharesLetters


horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

print("Problem 1:")
print(initialLetterCount(horton))

print("")
print("Problem 2:")
print(initialLetters(horton))

print("")
print("Problem 3:")
print(shareALetter(horton))
