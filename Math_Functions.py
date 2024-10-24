def min(x, y):
    # Returns the minimum of x and y
    if x != y:
        return x if x < y else y


def max(x, y):
    # Returns the maximum of x and y
    if x != y:
        return x if x > y else y


def abs(x):
    # Returns the absolute value of x
    if x < 0:
        return -x  # If x is negative, return its positive counterpart
    else:
        return x  # If x is non-negative, return x


def abs_max(x, y):
    # Returns the maximum of the absolute values of x and y
    x = abs(x)  # Get the absolute value of x
    y = abs(y)  # Get the absolute value of y
    if x != y:
        return x if x > y else y


def floor(x):
    # Returns the largest integer less than or equal to x
    if x == int(x):
        return int(x)  # If x is already an integer, return it
    elif x > 0:
        return int(x)  # If x is positive, return the integer part
    else:
        return int(x) - 1  # If x is negative, return the integer part minus one


def ceil(x):
    # Returns the smallest integer greater than or equal to x
    if x == int(x):
        return int(x)  # If x is already an integer, return it
    elif x > 0:
        return int(x) + 1  # If x is positive, return the integer part plus one
    else:
        return int(x)  # If x is negative, return the integer part


def square_root(x):
    # Returns the square root of x
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")  # Cannot take square root of a negative number
    return x ** 0.5  # Calculate and return the square root


def power(base, exponent):
    # Returns the result of base raised to the power of exponent
    return base ** exponent  # Calculate and return base raised to the exponent


def factorial(n):
    # Returns the factorial of n (n!)
    if n < 0:
        print("Factorial is not defined for negative numbers.")  # Factorial is not defined for negative numbers
    
    result = 1  # Initialize result to 1
    for i in range(2, n + 1):  # Iterate from 2 to n
        result *= i  # Multiply result by i
    return result  # Return the final factorial value





""" Summary of Functions:

    min(x, y): Returns the smaller of two values.
    
    max(x, y): Returns the larger of two values.
    
    abs(x): Returns the absolute value of a number.
    
    abs_max(x, y): Returns the maximum of the absolute values of two numbers.
    
    floor(x): Returns the largest integer less than or equal to a given number.
    
    ceil(x): Returns the smallest integer greater than or equal to a given number.
    
    square_root(x): Computes the square root of a number, raising an error for negative inputs.
    
    power(base, exponent): Raises a base to a given exponent.
    
    factorial(n): Computes the factorial of a non-negative integer. """
