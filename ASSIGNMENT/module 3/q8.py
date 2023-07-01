def list_to_string(char_list):
    string = ''.join(char_list)
    return string


characters = ['H', 'e', 'l', 'l', 'o']
result_string = list_to_string(characters)
print("List of characters:", characters)
print("Converted string:", result_string)
