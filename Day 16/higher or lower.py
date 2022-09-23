from art import logo
from art import vs
from game_data import data
import random

def famous_person():
    person_1 = random.choice(data)
    person_2 = random.choice(data)


famous_person()


def guessing_game(data):
    game_over = False
    points = 0
    while not game_over:
        print(logo)

        print(vs)

        answer = input("Which person do you think has the higher follower count, 'a' or 'b': ")
        if answer = "a" and a_choice > b_choice:
            points += 1
        elif answer = "a" and a_choice < b_choice:
            game_over = True
        elif answer = "b" and b_choice > a_choice:
            points += 1
        elif answer = "b" and b_choice < a_choice:
            game_over = True


guessing_game(data)
