def check_element_in_tuple(input_tuple, element):
    if element in input_tuple:
        return True
    else:
        return False


my_tuple = (1, 2, 3, 4, 5)
element_to_check = 3
result = check_element_in_tuple(my_tuple, element_to_check)
print("Tuple:", my_tuple)
print("Element to Check:", element_to_check)
print("Element Exists?", result)
