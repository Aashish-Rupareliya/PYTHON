def reverse_tuple(input_tuple):
    reversed_tuple = input_tuple[::-1]
    return reversed_tuple

my_tuple = (1, 2, 3, 4, 5)
reversed_result = reverse_tuple(my_tuple)
print("Original Tuple:", my_tuple)
print("Reversed Tuple:", reversed_result)
