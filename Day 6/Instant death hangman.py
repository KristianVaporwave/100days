import random

world_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(world_list)
num_of_v = len(chosen_word)
display = []

for letter in chosen_word:
    display += "_"
print(display)

print(f"Psst, the chosen word is {chosen_word}")

end_of_game = False

while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    lives = 5

    for position in range(num_of_v):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            lives -= 1
            print(f"You have {lives} left")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win!")

    if lives == 0:
        end_of_game = True
        print("You lose!")
