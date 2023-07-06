def find_highest_values(dictionary, n=3):
    sorted_values = sorted(dictionary.values(), reverse=True)
    highest_values = sorted_values[:n]
    return highest_values

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
highest_values = find_highest_values(my_dict, 3)
print("Dictionary:", my_dict)
print("Highest 3 Values:", highest_values)
