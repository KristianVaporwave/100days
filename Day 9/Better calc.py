from art import logo

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

print(logo)
num1 = int(input("What's the first number: "))


for symbol in operations:
    print(symbol)
symbol = (input("What function do you want? "))
num2 = int(input("What's the second number: "))
calculation_function = operations[symbol]
first_answer = calculation_function(num1, num2)


print(f"{num1} {symbol} {num2} = {first_answer}")


symbol = (input("What function do you want? "))
num3 = int(input("What's the next number: "))
calculation_function = operations[symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {symbol} {num3} = {second_answer}")