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

num1 = int(input("What's the first number: "))


for symbol in operations:
    print(symbol)
symbol = (input("What function do you want? "))
num2 = int(input("What's the second number: "))
calculation_function = operations[symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {symbol} {num2} = {answer}")


