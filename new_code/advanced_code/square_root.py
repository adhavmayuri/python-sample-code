import math

# Input a number
num = float(input("Enter a number: "))

# Calculate and print the square root
if num >= 0:
    square_root = math.sqrt(num)
    print(f"The square root of {num} is {square_root:.2f}")
else:
    print("Square root is not defined for negative numbers.")
