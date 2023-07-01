def is_list_empty(lst):
    if not lst:
        return True
    else:
        return False

empty_list = []
non_empty_list = [1, 2, 3]

print("Is empty_list empty?", is_list_empty(empty_list))             # Output: True
print("Is non_empty_list empty?", is_list_empty(non_empty_list))     # Output: False
