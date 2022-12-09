from art import logo

def add(n1, n2):
    return n1 + n2
    
def sub(n1, n2):
    return n1 - n2
    
def mul(n1, n2):
    return n1 * n2
    
def div(n1, n2):
    return n1 / n2

operations = {"+": add, "-": sub, "*": mul, "/": div}

def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while(True):
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if option == 'n':
            calculator()
        else:
            num1 = answer

calculator()
 