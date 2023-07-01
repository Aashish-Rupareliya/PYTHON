def remove_empty_tuples(tuple_list):
    return [t for t in tuple_list if t]


my_list = [(1, 2), (), (3, 4), (), (5, 6, 7), ()]
modified_list = remove_empty_tuples(my_list)
print("Original List:", my_list)
print("Modified List:", modified_list)
