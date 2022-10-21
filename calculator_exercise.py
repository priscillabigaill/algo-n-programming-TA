
# Create a calculator program using functions, loops, if and else.
# Basically everything u have learnt so far. 
# push ur answers to a repo and WA or Discord the link to me

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Simple Calculator\n\n1.addition(+)\n2.substraction(-)\n3.multlipication(x)\n4.division(:)\n")

while True:

    operator = input("Pick an operator (using the symbol): ")
    first = input("Input first number: ")
    second = input("Input second number: ")

    if operator == "+":
        print(first, "+", second, "=", int(first) + int(second))
    elif operator == "-":
        print(first, "-", second, "=", int(first) - int(second))
    elif operator == "x":
        print(first, "x", second, "=", int(first) * int(second))
    elif operator == ":":
        print(first, ":", second, "=", int(first) / int(second))
    else:
        print("Operator is not supported")

    again = input("Go again? Yes/No: ")

    if again == "Yes" or again == "yes":
        continue
    if again == "No" or again == "no":
        break
