"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 10 - November 5th, 2019
"""
import string


def file_copy(in_file, out_file):
    inFile = open(in_file)
    outFile = open(out_file, 'w')

    for line in inFile:
        outFile.write(line)

    inFile.close()
    outFile.close()


def file_stats(in_file):
    inFile = open(in_file)
    lines = 0
    words = 0
    characters = 0

    for line in inFile:
        lines += 1
        words += len(line.split(' '))
        characters += len(line)

    inFile.close()
    print("Lines:", lines)
    print("Words:", words)
    print("Characters:", characters)


def repeat_words(in_file, out_file):
    inFile = open(in_file)
    outFile = open(out_file, 'w')

    for line in inFile:
        repeatedList = []
        line = line.lower()
        line = "".join(l for l in line if l not in string.punctuation)
        wordList = line.split(' ')
        for word in line.split(' '):
            if wordList.count(word) > 1 and word not in repeatedList:
                repeatedList.append(word)
        if len(repeatedList) != 0:
            for repeated in repeatedList:
                outFile.write(repeated + " ")
            outFile.write("\n")

    inFile.close()
    outFile.close()


file_copy('created_equal.txt', 'copy.txt')
copy_f = open('copy.txt')
copy_f.read()

file_stats('created_equal.txt')

inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)
