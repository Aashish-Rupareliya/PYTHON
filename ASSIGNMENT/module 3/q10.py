def find_second_smallest(numbers):
    # Check if the list has at least two elements
    if len(numbers) < 2:
        return None

    # Find the minimum and second minimum
    minimum = float('inf')
    second_minimum = float('inf')
    
    for num in numbers:
        if num < minimum:
            second_minimum = minimum
            minimum = num
        elif num < second_minimum and num != minimum:
            second_minimum = num

    # Return the second minimum
    return second_minimum


# Example usage:
my_list = [5, 2, 8, 3, 1, 7, 4, 6]
second_smallest = find_second_smallest(my_list)
print("List of numbers:", my_list)
print("Second smallest number:", second_smallest)
