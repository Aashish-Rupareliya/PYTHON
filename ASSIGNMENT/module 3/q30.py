def print_unique_values(dictionary):
    unique_values = set(dictionary.values())
    for value in unique_values:
        print(value)


# Example usage:
my_dict = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}
print("Dictionary:", my_dict)
print("Unique Values:")
print_unique_values(my_dict)
