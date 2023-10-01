# main.py

import factorial_module

try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        raise ValueError("Please enter a non-negative integer.")
    
    result = factorial_module.factorial(num)
    print(f"The factorial of {num} is {result}")
except ValueError as ve:
    print(ve)
