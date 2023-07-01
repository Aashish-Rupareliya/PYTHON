def convert_tuple_to_string(input_tuple):
    string_representation = ''.join(str(element) for element in input_tuple)
    return string_representation


my_tuple = (1, 2, 3, 4, 5)
string_result = convert_tuple_to_string(my_tuple)
print("Original Tuple:", my_tuple)
print("String Representation:", string_result)
