def minDifference(arr):
    abs_sum = 0
    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr) - 1):
        abs_sum = abs_sum + abs(sorted_arr[i] - sorted_arr[i + 1])
    return abs_sum
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = minDifference(my_list)
print("Minimum absolute difference:", result)
