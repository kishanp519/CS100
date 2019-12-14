# 1-10
# b a c a d c b a c e

# 11A
def pentagon(t, side):
    t.down()
    for i in range(5):
        t.forward(side)
        t.right(360 / 5)


# 11B
def pentagons(t, length, delta, num, angle):
    for i in range(num):
        pentagon(t, length + (delta * i))
        # pentagon(t, length)
        # length += delta
        t.right(angle)


# 12
def filter(d, kFilter, vFilter):
    new = {}
    for key in d:
        if key < kFilter and d[key] < vFilter:
            new[key] = d[key]
    return new


# 13
def pigLatin(inFile, outFile):
    inF = open(inFile)
    outF = open(outFile, 'w')
    for line in inF:
        for word in line.split():
            if word[0] in 'aeiou':
                outF.write(word + 'ay ')
            else:
                outF.write(word[1:] + word[0] + 'ay ')
        outF.write('\n')
    inF.close()
    outF.close()
