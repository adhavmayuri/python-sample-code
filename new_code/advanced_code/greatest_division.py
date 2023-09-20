def Division(num1, num2):
    for num in range(max(num1, num2), 0, -1):
        if num1 % num == 0 and num2 % num == 0:
            return num

# Example usage:
result = Division(18, 24)
print(result)  
