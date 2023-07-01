def count_substring_occurrences(string, substring):
    count = 0
    start_index = 0

    while True:
        index = string.find(substring, start_index)
        if index != -1:
            count += 1
            start_index = index + 1
        else:
            break

    return count

# Example usage
input_string = input("Enter a string: ")
input_substring = input("Enter a substring: ")
occurrences = count_substring_occurrences(input_string, input_substring)
print(f"The substring '{input_substring}' occurs {occurrences} times in the string.")
