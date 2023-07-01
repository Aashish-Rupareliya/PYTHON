def get_unique_elements(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = get_unique_elements(my_list)
print("Original list:", my_list)
print("List with unique elements:", unique_list)
