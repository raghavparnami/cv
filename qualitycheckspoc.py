# This is a sample Python code with intentional quality issues

# Check Comments:
# This function calculates the square of a number
def square(num):
    return num ** 2

# Check Docstrings:
def add(a, b):
    """This function adds two numbers"""
    return a + b

# Check Function Names:
def subtract(x, y):
    return x - y

# Check Variable Naming:
a = 10
b = 20

# Check Indentation:
if a > b:
result = a - b
else:
    result = b - a

# Check Function Complexity:
def fibonacci(n):
    """This function calculates the nth Fibonacci number"""
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
