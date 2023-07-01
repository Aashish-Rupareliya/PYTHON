def get_list_stats(lst):
    if len(lst) == 0:
        return None  # Return None if the list is empty

    smallest = largest = lst[0]
    total_sum = 0

    for num in lst:
        total_sum += num

        if num < smallest:
            smallest = num

        if num > largest:
            largest = num

    return largest, smallest, total_sum


# Example usage
numbers = [7, 2, 9, 1, 5]
largest_num, smallest_num, sum_of_all = get_list_stats(numbers)

print("List:", numbers)
print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", sum_of_all)
