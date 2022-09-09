print("Welcome to the Love Calculator!")
name1 = input("Enter your name: \n")
name2 = input("Enter their name: \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

combined_name = lower_name2 + lower_name1

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")

true = t + r + u + e
love = l + o + v + e
#TRUE LOVE

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"You are okay together, your score is {score}")
else:
    print("You are terrible together")

