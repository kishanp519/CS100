"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 11 - December 5th, 2019
"""


def safeOpen(filename):
    try:
        file = open(filename)
        return file
    except:
        return


def safeFloat(x):
    try:
        return float(x)
    except:
        return 0.0


def averageSpeed():
    fileName = input("Enter file name to process: ")
    file = safeOpen(fileName)

    if file is None:
        print("The file you entered is invalid. Try again.")
        fileName = input("Enter file name to process: ")
        file = safeOpen(fileName)

        if file is None:
            print("The file you entered is invalid. You cannot try again.")
            return

    total = 0
    count = 0
    for line in file:
        for each in line.split(" "):
            val = safeFloat(each)
            if val > 2.0:
                total += val
                count += 1

    file.close()

    average = total / count
    print("Average speed is " + str(round(average, 2)) + " miles per hour.")


averageSpeed()
