try:
    # Perform some operations that may raise an exception
    num1 = 10
    num2 = 0
    result = num1 / num2  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the ZeroDivisionError exception
    print("Division by zero is not allowed.")
except Exception as e:
    # Handle other exceptions if needed
    print("An error occurred:", str(e))
finally:
    # This block will always run, whether there's an exception or not
    print("The 'finally' block always executes.")
    
