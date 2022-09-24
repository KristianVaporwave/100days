from art import logo
from art import vs
from game_data import data
import random


def guessing_game():
    game_over = False
    points = 0

    while not game_over:
        account_a = random.choice(data)
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        account_name_a = account_a["name"]
        account_fc_a = account_a["follower_count"]
        account_dc_a = account_a["description"]
        account_country_a = account_a["country"]
        account_name_b = account_b["name"]
        account_fc_b = account_b["follower_count"]
        account_dc_b = account_b["description"]
        account_country_b = account_b["country"]

        print(logo)
        print(f"Compare A: {account_name_a}, a {account_dc_a}, from {account_country_a}.")
        print(vs)
        print(f"Against B: {account_name_b}, a {account_dc_b}, from {account_country_b}.")

        answer = input("Which person do you think has the higher follower count, 'a' or 'b': ")
        if answer == "a" and account_fc_a > account_fc_b:
            points += 1
            print(f"You're right, your score is: {points}.")
        elif answer == "a" and account_fc_a < account_fc_b:
            game_over = True
            print(f"You lost, your final score is: {points}.")
        elif answer == "b" and account_fc_b > account_fc_a:
            points += 1
            print(f"You're right, your score is: {points}.")
        elif answer == "b" and account_fc_b < account_fc_a:
            game_over = True
            print(f"You lost, your final score is: {points}.")

guessing_game()
