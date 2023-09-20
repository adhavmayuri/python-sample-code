def SecondGreatLow(arr):
    multiples_removed_list = list(set(arr))
    sorted_list = sorted(multiples_removed_list)

    second_greatest = sorted_list[-2]
    second_lowest = sorted_list[1]

    return "%d %d" % (second_lowest, second_greatest)

# Example usage:
input_list = [7, 7, 12, 98, 106]
result = SecondGreatLow(input_list)
print(result)  #
