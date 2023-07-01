def split_list_to_variables(input_list):
    if len(input_list) < 3:
        print("Error: List must contain at least 3 elements")
        return

    var1, var2, *var3 = input_list[:3]
    print("Variable 1:", var1)
    print("Variable 2:", var2)
    print("Variable 3 and onwards:", var3)


my_list = [1, 2, 3, 4, 5, 6]
print("Original list:", my_list)
split_list_to_variables(my_list)
