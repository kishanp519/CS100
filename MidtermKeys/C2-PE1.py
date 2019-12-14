##1. b
##2. B
##3. C
##4. A
##5. E
##6. D
##7. A
##8. D
##9. B
##10. C

##11a
import turtle

t = turtle.Turtle()


def drawSquare(t, Length):
    t.pendown()
    for i in range(4):
        t.forward(Length)
        t.right(90)


# 11b
def offsetSquares(t, Length, num, xoffset, yoffset):
    for i in range(num):
        drawSquare(t, Length)
        t.penup()
        t.forward(xoffset)
        t.right(90)
        t.forward(yoffset)
        t.left(90)


# 12
def indexByLength(s):
    words = s.split()
    res = {}
    for word in words:
        keylen = len(word)
        if keylen not in res:
            res[keylen] = [word]
        elif word not in res[keylen]:
            res[keylen].append(word)
    return res


# 13
def cloneLines(inFile, outFile):
    inF = open(inFile)
    outF = open(outFile, "w")
    for line in inF:
        words = line.split()
        for word in words:
            if words.count(word) > 1:
                outF.write(line)
                break
    inF.close()
    outF.close()
