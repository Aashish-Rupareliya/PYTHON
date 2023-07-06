import itertools

def display_letter_combinations(dictionary):
    keys = sorted(dictionary.keys())
    combinations = list(itertools.product(*(dictionary[key] for key in keys)))
    for combination in combinations:
        print(''.join(combination))


# Example usage:
data = {'1': ['a', 'b'], '2': ['c', 'd']}
print("Sample data:", data)
print("Expected Output:")
display_letter_combinations(data)
