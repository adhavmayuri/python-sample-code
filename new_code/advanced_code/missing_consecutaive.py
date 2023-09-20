def Consecutive(an_array):
    an_array.sort()
    maximum = max(an_array)
    minimum = min(an_array)

    missing_nums = []
    for num in range(minimum, maximum):
        if num not in an_array:
            missing_nums.append(num)

    return len(missing_nums)

# Example usage:
result = Consecutive([4, 2, 1, 6, 5])
print(result)  