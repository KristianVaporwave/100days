import random
from random import sample
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards(random_cards):
    user_cards = random.choices(cards, k=2)
    user_score = sum(sample(user_cards, 2))
    dealer_cards = random.choices(cards, k=2)
    dealer_score = sum(sample(dealer_cards, 2))


    print(logo)
    print(f"Your cards are: {user_cards}, current score is: {user_score}")
    print(f"Computer's first card is: {dealer_cards}")

    should_continue = True
    while should_continue:
        if user_score == 21 and dealer_score != 21:
            print("You win")
            play_again = input("Do you want to play again? y/n: ")
            if play_again == "y":
                deal_cards(random_cards)
            else:
                should_continue = False
        elif dealer_score == 21 and user_score != 21:
            print("You lose")
            should_continue = False
            play_again = input("Do you want to play again? y/n: ")
            if play_again == "y":
                deal_cards(random_cards)
            else:
                should_continue = False
        elif user_score == 21 and dealer_score == 21:
            print("It's a draw")
            should_continue = False
            play_again = input("Do you want to play again? y/n: ")
            if play_again == "y":
                deal_cards(random_cards)
            else:
                should_continue = False
        elif user_score > 21 and  cards.count(11):
            ace_exchange = input("You will be bust if ace stays 11, do you want to switch? y/n: ")
                if ace_exchange == "y":



deal_cards(random_cards=cards)