def is_sublist(list1, sublist):
    if len(sublist) == 0:
        return True
    if len(sublist) > len(list1):
        return False
    for i in range(len(list1) - len(sublist) + 1):
        if list1[i:i+len(sublist)] == sublist:
            return True
    return False


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list1 = [3, 4, 5]
sub_list2 = [8, 9, 10]
sub_list3 = [2, 3, 4, 5, 6]
print("List:", my_list)
print("Sublist 1:", sub_list1)
print("Is sublist 1 present?", is_sublist(my_list, sub_list1))
print("Sublist 2:", sub_list2)
print("Is sublist 2 present?", is_sublist(my_list, sub_list2))
print("Sublist 3:", sub_list3)
print("Is sublist 3 present?", is_sublist(my_list, sub_list3))
