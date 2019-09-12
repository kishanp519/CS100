"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 02 - September 17th, 2019
"""

grades = ["B", "D", "A", "C", "A", "F", "B", "F", "C", "A"]
gradeFrequency = [grades.count("A"), grades.count("B"), grades.count("C"), grades.count("D"), grades.count("F")]

print("Grades:", grades)
print("Frequency of Grades:", gradeFrequency)

print("")

dog_breeds = ["collie", "sheepdog", "Chow", "Chihuahua"]
herding_dogs = dog_breeds[0:2]
tiny_dogs = [dog_breeds[-1]]
containsPersian = "Persian" in dog_breeds

print("Dog Breeds:", dog_breeds)
print("Herding Dogs:", herding_dogs)
print("Tiny Dogs:", tiny_dogs)
print("Is 'Persian' in the list of dog breeds?:", containsPersian)
