def unzip_list_of_tuples(tuple_list):
    unzipped_lists = list(zip(*tuple_list))
    return unzipped_lists

my_list = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
unzipped_lists = unzip_list_of_tuples(my_list)
print("Original List of Tuples:", my_list)
print("Unzipped Lists:", unzipped_lists)
