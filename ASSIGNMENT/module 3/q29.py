from collections import Counter

def combine_dictionaries(d1, d2):
    combined_dict = Counter(d1) + Counter(d2)
    return combined_dict


# Example usage:
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dictionary = combine_dictionaries(d1, d2)
print("Dictionary 1:", d1)
print("Dictionary 2:", d2)
print("Combined Dictionary:", combined_dictionary)
