def remove_duplicates(lst):
    return list(set(lst))

my_list = [1, 2, 3, 2, 4, 1, 5, 3]
result = remove_duplicates(my_list)
print("List with duplicates removed:", result)
