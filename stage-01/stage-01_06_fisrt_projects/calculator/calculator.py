def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b

print("=== CLI Calculator ===")

while True:

    try:
        first_number = float(input("\nEnter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        if operator == "+":
            result = add(first_number, second_number)

        elif operator == "-":
            result = subtract(first_number, second_number)

        elif operator == "*":
            result = multiply(first_number, second_number)

        elif operator == "/":
            result = divide(first_number, second_number)

        else:
            print("Invalid operator.")
            continue

        print(f"Result: {result}")

    except ValueError as error:
        print(f"Error: {error}")

    choice = input("\nDo you want to calculate again? (y/n): ").lower()

    if choice != "y":
        print("Calculator closed.")
        break