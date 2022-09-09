import random

print("Welcome to the rock, paper, scissors game!")
choice = input("Please choose one of the following: rock, paper, scissors: \n")

rock = '''
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_choice = random.randint(1, 3)

if random_choice == 1:
    print(rock)
    if choice == "rock":
        print("Tied")
    elif choice == "scissors":
        print("You lose!")
    else:
        print("You win!")
elif random_choice == 2:
    print(paper)
    if choice == "paper":
        print("Tied")
    elif choice == "rock":
        print("You lose!")
    else:
        print("You win!")
else:
    print(scissors)
    if choice == "scissors":
        print("Tied")
    elif choice == "paper":
        print("You lose!")
    else:
        print("You win!")
