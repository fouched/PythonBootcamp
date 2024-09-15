
def calculate(prev) -> float:

    if prev == "":
        num1 = float(input("What's the first number: "))
    else:
        num1 = float(prev)

    num2 = float(input("What's the next number: "))
    op = input("Choose operation: ")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        result = num1 / num2
    else:
        result = num1 * num2

    print(f"Result {result}\n")

    c = input(f"Type 'y' to continue with {result}, type 'n' to start a new calculation, or e to exit: ")
    if c == "y":
        calculate(result)
    elif c == "e":
        print("Goodbye!")
    else:
        calculate("")


calculate("")