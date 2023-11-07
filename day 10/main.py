from logo import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    should_continue = True
    while should_continue:
        print("================operation:==================".title())
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above:")
        if operation_symbol not in operations:
            print("Invalid operation")
            continue
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "y":
            num1 = answer
        elif input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "n":
            should_continue = False
            print("Goodbye")
        else:
            print("Invalid input")


calculator()
