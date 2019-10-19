#Multiple Choice 1-10:
#e a a e b b d c c e

#11A
def squareWave(t, length):
    t.down()
    t.fd(length)
    t.rt(45)
    t.fd(length)
    t.lt(45)
    t.fd(length)
    t.lt(45)
    t.fd(length)
    t.rt(45)
    t.fd(length)

#11B
def motif(t, length, num, angle):
    for i in range(num):
        squareWave(t, length)
        t.rt(angle)

#12
def getDivergent(words):
    c = 0
    for word in words:
        if word[0] == word[-1]:
            c += 1
    return (c, len(words) - c)

#13
def printLines(line):
    num = int(input("Number of repetitions? "))
    for i in range(num):
        print(line)
    return num
