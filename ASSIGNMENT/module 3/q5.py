def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = [3, 10, 12, 15]

print(has_common_member(list_a, list_b))  # Output: False
print(has_common_member(list_a, list_c))  # Output: True
