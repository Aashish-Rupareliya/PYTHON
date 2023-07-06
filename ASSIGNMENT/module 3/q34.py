from collections import Counter

def create_dictionary_from_string(input_string):
    letter_count = Counter(input_string)
    return dict(letter_count)


input_str = 'aashish123'
result_dict = create_dictionary_from_string(input_str)
print("Sample string:", input_str)
print("Expected Output:")
print(result_dict)
