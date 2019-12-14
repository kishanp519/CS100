# 1-10
# b e b c e d d d c c

# 11A
class CollegeDirectory:
    '''a directory containing the names and emails of students'''

    def __init__(self, name):
        self.name = name
        self.students = {}

    def addStudent(self, studentName, emailAddress):
        self.students[studentName] = emailAddress

    def getEmailList(self):
        l = []
        for student in self.students:
            l.append("{} <{}>".format(student, self.students[student]))
        return l


# 11B
import college_directory

haw = college_directory.CollegeDirectory("Hawthorne")
haw.addStudent("Hester Prynne", "hprynne@hawthorne.edu")
haw.addStudent("Roger Chillingworth", "rchillingworth@hawthorne.edu")
print(haw.getEmailList())


# 12
def starCounter(starDictionary, maxDistance, classification):
    res = 0
    for star in starDictionary:
        if starDictionary[star]['distance'] < maxDistance and starDictionary[star]['type'] == classification:
            res += 1
    return res


# 13
def lineStats(inFile, outFile, threshold):
    inF = open(inFile)
    outF = open(outFile, 'w')
    for line in inF:
        longs = 0
        caps = 0
        for word in line.split():
            if len(word) >= threshold:
                longs += 1
            if word[0] == word[0].upper():
                caps += 1
        outF.write(long + " " + caps + "\n")
    inF.close()
    outF.close()
