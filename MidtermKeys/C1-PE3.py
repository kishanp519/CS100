#1-10
#c c e d e b c b a d

#11A
def stair(t, tread_size, riser_height):
    t.pendown()
    t.forward(tread_size)
    t.right(90)
    t.forward(riser_height)
    t.left(90)

#11B
def staircase(t, num_stairs, tread_size, riser_height):
    for i in range(num_stairs):
        stair(t, tread_size, riser_height)

#12
def vowel_tracker(words):
    ret = [0, 0]
    vowels = 'aeiouAEIOU'
    for word in words:
        if word[0] in vowels:
            ret[0] += 1
        if word[-1] in vowels:
            ret[1] += 1
    return ret

#13
def month_info(medium_length):
    month = input("What month is it? ")
    days = int(input("How many days in " + month + "? "))
    if days < medium_length:
        print(month + " is short")
    elif days > medium_length:
        print(month + " is long")
    else:
        print(month + " is medium")
    return month
