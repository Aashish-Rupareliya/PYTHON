def find_repeated_items(input_tuple):
    repeated_items = []
    for item in input_tuple:
        if input_tuple.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items


my_tuple = (1, 2, 3, 4, 2, 5, 4, 6, 7, 1)
repeated_items = find_repeated_items(my_tuple)
print("Tuple:", my_tuple)
print("Repeated Items:", repeated_items)
