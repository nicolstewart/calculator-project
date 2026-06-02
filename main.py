import art

#creating the necessary functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#adding functions to dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#getting user input
def calculator():
    print(art.logo)
    repeat_answer = True
    num1 = float(input("Enter a number: "))

    while repeat_answer:
        for symbol in operations:
            print(symbol)
        user_operation = input("Choose an operation: ")
        num2 = float(input("Enter your second number: "))
        answer = operations[user_operation](num1, num2)
        print(f"{num1} {user_operation} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")

        if choice == "y":
            num1 = answer
        else:
            repeat_answer = False
            print("\n" * 20)
            calculator()

calculator()