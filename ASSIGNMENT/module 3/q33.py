from collections import Counter

def combine_values(dictionary_list):
    combined_dict = Counter()
    for dictionary in dictionary_list:
        combined_dict[dictionary['item']] += dictionary['amount']
    return combined_dict

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
combined_values = combine_values(data)
print("Sample data:", data)
print("Expected Output:")
print(combined_values)
