def turn_right():
    turn_left()
    turn_left()
    turn_left()

def single_jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() == False:
    if wall_in_front():
        single_jump()
    else:
        move()

