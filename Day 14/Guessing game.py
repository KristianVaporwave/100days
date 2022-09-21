import random
from art import logo

random_number = random.randint(1, 99)

print(logo)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 99")
print(f"Pssst, the correct number is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def game_difficulty():
    number_of_guesses = 0
    if difficulty == "easy":
        return number_of_guesses + 10
    else:
        return number_of_guesses + 4

def guessing_game(number_of_guesses):
    game_is_over = False
    print(f"\nYou have {number_of_guesses} attempts to guess the number.")
    while not game_is_over:
        player_guess = int(input("Make a guess: "))
        if player_guess == random_number:
            print("That is the correct number!")
            game_is_over = True
        elif player_guess > random_number:
            print("Too high. \nGuess again.")
            number_of_guesses -= 1
            print(f"\nYou have {number_of_guesses} attempts to guess the number.")
            if number_of_guesses == 0:
                print("You lost")
                game_is_over = True
        elif player_guess < random_number:
            print("Too low. \nGuess again.")
            number_of_guesses -= 1
            print(f"\nYou have {number_of_guesses} attempts to guess the number.")
            if number_of_guesses == 0:
                print("You lost")
                game_is_over = True


guessing_game(number_of_guesses=game_difficulty())






