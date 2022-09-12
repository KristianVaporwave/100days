def turn_right():
    turn_left()
    turn_left()
    turn_left()


def steps():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
    if front_is_clear() == True:
        move()
    else:
        steps()