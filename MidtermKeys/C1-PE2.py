#Multiple Choice 1-10:
#e b e a a d a d b b

#11A
def rhombus(t, side, acuteAngle):
    t.down()
    for i in range(2):
        t.fd(side)
        t.rt(acuteAngle)
        t.fd(side)
        t.rt(180-acuteAngle)

#11B
def rhombuses(t, side, acuteAngle, count, rotation):
    for i in range(count):
        rhombus(t, side, acuteAngle)
        t.rt(rotation)

#12
def first_last(string_list):
    ret=[]
    for item in string_list:
        if len(item)>0 and item[0]==item[-1]:
            ret.append(item)
    return ret

#13
def number_luck(lucky, unlucky):
    user = int(input("Give me a number from 2 to 12: "))
    if user in lucky:
        print(user, "is lucky. You win!")
    elif user in unlucky:
        print(user, "is not lucky. You lose!")
    else:
        print(user, "is boring.")
    return user
