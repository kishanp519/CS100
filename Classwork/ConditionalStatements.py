"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 8 - September 26th, 2019
"""


age = int(input("What's your age?: "))

if age < 0 or age > 120:
    print("You have entered an invalid age.")
elif age >= 18:
    print("You are old enough to vote, Congratulations!")
else:
    print("You are too young to vote.")

print("Goodbye!")

score = int(input("Enter your exam score: "))

if score >= 90:
    print("You received an 'A' on the exam.")
elif score >= 80:
    print("You received a 'B' on the exam.")
elif score >= 70:
    print("You received a 'C' on the exam.")
elif score >= 60:
    print("You received a 'D' on the exam.")
else:
    print("You received an 'F' on the exam.")

counter = 0
scores = [98, 72, 88, 92, 80]
aGrades = []
for score in scores:
    if score > 90:
        aGrades.append(score)
        counter += 1

print("Amount of A's:", counter)
print("Grades:", aGrades)

nameList = ["John", "Jake", "David", "Abakir", "Brain"]
initials = ""

for name in nameList:
    initials += name[0] + "" + name[-1]

print(initials)

counter = 0
for name in nameList:
    if len(name) > 4:
        continue
    if "a" in name:
        counter += 1

print("'a' Counter:", counter)

message = "how are you"
vowels = ['a', 'e', 'i', 'o', 'u']
counter = 0;

for i in range(len(message)):
    for vow in vowels:
        if message[i] == vow:
            counter += 1

print("Vowel Counter:", counter)

vowelPositions = []
for i in range(len(message)):
    for vow in vowels:
        if message[i] == vow:
            vowelPositions.append(i)

print("Positions:", vowelPositions)





