def convert_to_dictionary(tuple_list):
    dictionary = dict(tuple_list)
    return dictionary


my_list = [("a", 1), ("b", 2), ("c", 3)]
my_dictionary = convert_to_dictionary(my_list)
print("Original List of Tuples:", my_list)
print("Dictionary:", my_dictionary)
