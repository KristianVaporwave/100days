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


def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        symbol = (input("Pick an operation: "))
        num2 = float(input("What's the second number: "))
        calculation_function = operations[symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"Type y if you want to continue with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()