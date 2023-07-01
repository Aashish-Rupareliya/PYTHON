def replace_last_value(tuples_list, new_value):
    modified_list = [tuple[:-1] + (new_value,) for tuple in tuples_list]
    return modified_list


my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
modified_list = replace_last_value(my_list, new_value)
print("Original List:", my_list)
print("Modified List:", modified_list)
