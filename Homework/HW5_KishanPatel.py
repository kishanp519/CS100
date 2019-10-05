"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 05 - October 5th, 2019
"""

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

print("Months that start with 'J':")
for month in months:
    if month[0] == "J":
        print("-", month)

print("")
print("Numbers that are divisible by 2 and 5:")
for number in range(0, 100):
    if number % 2 == 0 and number % 5 == 0:
        print("-", number)

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

description = "Vowels in '" + horton + "'"
print("")
print(description)
for eachLetter in range(len(horton)):
    for vowel in range(len(vowels)):
        if horton[eachLetter] == vowels[vowel]:
            print("-", vowels[vowel])


