print("Welcome to calculator")

x = float(input("First number: "))
y = float(input("Second number: "))

op = input("Operator (+|-|*|/): ")


def add(x, y):
    """
    Add two numbers together.
    Parameters:
        x (int or float): The first number.
        y (int or float): The second number.
    Returns:
        int or float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first number.
    Parameters:
        x (float): The number to be subtracted from.
        y (float): The number to subtract.
    Returns:
        float: The result of the subtraction.
    """

    return x - y

def multiply(x, y): 
    """
    Multiplies two numbers together.
    Parameters:
        x (int or float): The first number.
        y (int or float): The second number.
    Returns:
        int or float: The product of x and y.
    """

    return x * y

def divide(x, y): 
    """
    Divide two numbers.
    Parameters:
        x (float): The numerator.
        y (float): The denominator.
    Returns:
        float: The result of the division.
    Raises:
        ZeroDivisionError: If the denominator is zero.
    """

    return x / y

result = 0
if op == "+":
    result = add(x, y)
elif op == "-":
    result = subtract(x, y)
elif op == "*":
    result = multiply(x, y)
elif op == "/":
    result = divide(x, y)

print (f"{x} {op} {y} = {result}")
