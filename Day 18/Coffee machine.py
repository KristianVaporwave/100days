from game_data import MENU
from art import logo
def coffee_machine():
    machine_off = False
    water_m = 300
    milk_m = 200
    coffee_m = 100
    money = 0

    while not machine_off:
        print(logo)
        order = input("What would you like (espresso/latte/cappuccino): ")
        if order == "off":
            print("The coffee machine will turn off now. ")
            machine_off = True
        if order == "report":
            print(f"Water: {water_m}ml")
            print(f"Milk: {milk_m}ml")
            print(f"Coffee: {coffee_m}g")
            print(f"Money: {money}$")
        if order == "espresso":
            if water_m >= MENU["espresso"]["ingredients"]["water"] and coffee_m >= MENU["espresso"]["ingredients"]["coffee"]:
                print("Please insert coins for your order, the cost is: 1.5$.")
                quarters = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickles = int(input("How many nickles: "))
                pennies = int(input("How many pennies: "))
                money_paid = quarters*0.5 + dimes*0.1 + nickles*0.05 + pennies*0.01
                if money_paid < MENU["espresso"]["cost"]:
                    print("Not enough money.")
                else:
                    change_back = money_paid - MENU["espresso"]["cost"]
                    water_m -= 50
                    coffee_m -= 18
                    money += 1.5
                    print(f"Here is {change_back}$ in change.")
                    print("Here is your espresso: ☕. Enjoy!")
            elif water_m < MENU["espresso"]["ingredients"]["water"] and coffee_m >= MENU["espresso"]["ingredients"]["coffee"]:
                print("There is not enough water.")
            elif water_m >= MENU["espresso"]["ingredients"]["water"] and coffee_m < MENU["espresso"]["ingredients"]["coffee"]:
                print("There is not enough coffee")
            elif water_m < MENU["espresso"]["ingredients"]["water"] and coffee_m < MENU["espresso"]["ingredients"]["coffee"]:
                print("There isn't enough water or coffee to make this.")
        if order == "latte":
            if water_m >= MENU["latte"]["ingredients"]["water"] and coffee_m >= MENU["latte"]["ingredients"]["coffee"] and milk_m >= MENU["latte"]["ingredients"]["milk"] :
                print("Please insert coins for your order, the cost is: 2.5$.")
                quarters = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickles = int(input("How many nickles: "))
                pennies = int(input("How many pennies: "))
                money_paid = quarters*0.5 + dimes*0.1 + nickles*0.05 + pennies*0.01
                if money_paid < MENU["latte"]["cost"]:
                    print("Not enough money.")
                change_back = money_paid - MENU["latte"]["cost"]
                water_m -= 250
                milk_m -= 150
                coffee_m -= 24
                money += 1.5
                print(f"Here is {change_back}$ in change.")
                print("Here is your latte: ☕. Enjoy!")
            elif water_m < MENU["latte"]["ingredients"]["water"] and coffee_m >= MENU["latte"]["ingredients"]["coffee"] and milk_m >= MENU["latte"]["ingredients"]["milk"]:
                print("There is not enough water.")
            elif water_m >= MENU["latte"]["ingredients"]["water"] and coffee_m < MENU["latte"]["ingredients"]["coffee"] and milk_m >= MENU["latte"]["ingredients"]["milk"]:
                print("There is not enough coffee")
            elif water_m >= MENU["latte"]["ingredients"]["water"] and coffee_m < MENU["latte"]["ingredients"]["coffee"] and milk_m >= MENU["latte"]["ingredients"]["milk"]:
                print("There is not enough milk")
            elif water_m < MENU["latte"]["ingredients"]["water"] and coffee_m < MENU["latte"]["ingredients"]["coffee"] and milk_m >= MENU["latte"]["ingredients"]["milk"]:
                print("There isn't enough water or coffee to make this.")
            else:
                print("There isn't ingredients to make this ")
        if order == "cappuccino":
            if water_m >= MENU["cappuccino"]["ingredients"]["water"] and coffee_m >= MENU["cappuccino"]["ingredients"]["coffee"] and milk_m >= MENU["cappuccino"]["ingredients"]["milk"] :
                print("Please insert coins for your order, the cost is: 2.5$.")
                quarters = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickles = int(input("How many nickles: "))
                pennies = int(input("How many pennies: "))
                money_paid = quarters*0.5 + dimes*0.1 + nickles*0.05 + pennies*0.01
                if money_paid < MENU["cappuccino"]["cost"]:
                    print("Not enough money.")
                change_back = money_paid - MENU["cappuccino"]["cost"]
                water_m -= 250
                milk_m -= 150
                coffee_m -= 24
                money += 1.5
                print(f"Here is {change_back}$ in change.")
                print("Here is your cappuccino: ☕. Enjoy!")
            elif water_m < MENU["cappuccino"]["ingredients"]["water"] and coffee_m >= MENU["cappuccino"]["ingredients"]["coffee"] and milk_m >= MENU["cappuccino"]["ingredients"]["milk"]:
                print("There is not enough water.")
            elif water_m >= MENU["cappuccino"]["ingredients"]["water"] and coffee_m < MENU["cappuccino"]["ingredients"]["coffee"] and milk_m >= MENU["cappuccino"]["ingredients"]["milk"]:
                print("There is not enough coffee")
            elif water_m >= MENU["cappuccino"]["ingredients"]["water"] and coffee_m < MENU["cappuccino"]["ingredients"]["coffee"] and milk_m >= MENU["cappuccino"]["ingredients"]["milk"]:
                print("There is not enough milk")
            elif water_m < MENU["cappuccino"]["ingredients"]["water"] and coffee_m < MENU["cappuccino"]["ingredients"]["coffee"] and milk_m >= MENU["cappuccino"]["ingredients"]["milk"]:
                print("There isn't enough water or coffee to make this.")
            else:
                print("There isn't ingredients to make this.")

coffee_machine()