word = "mealice"
letter = "a"

while letter in word:
    word = word[:-1]
    print(word)
    print(letter + ' ')
