"""
Kishan Patel
CS 100 - Section 019, Fall 2019
Lecture 5 - September 17th, 2019
"""

scores = [int(input("Enter your exam grade for Exam #1: ")), int(input("Enter your exam grade for Exam #2: ")),
          int(input("Enter your exam grade for Exam #3: ")), int(input("Enter your exam grade for Exam #4: ")),
          int(input("Enter your exam grade for Exam #5: "))]

average = sum(scores) / len(scores)
frequency = scores.count(100)

print("Scores: ", scores)
print("Average: ", average)
print("Frequency of '100':", frequency)
