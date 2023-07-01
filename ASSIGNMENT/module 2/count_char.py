def count_character_frequency(string):
    frequency = {}

    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


input_string = input("Enter a string: ")
result = count_character_frequency(input_string)
print("Character frequency:")
for char in result:
    print(f"{char}: {result[char]}")
