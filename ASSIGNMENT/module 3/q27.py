def check_multiple_keys_exist(dictionary, keys):
    return all(key in dictionary for key in keys)


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'b', 'e']
result = check_multiple_keys_exist(my_dict, keys_to_check)
print("Dictionary:", my_dict)
print("Keys to Check:", keys_to_check)
print("All keys exist:", result)
