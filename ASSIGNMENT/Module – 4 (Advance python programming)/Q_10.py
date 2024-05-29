from collections import Counter

def word_frequency(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)

print(word_frequency('Q_1.txt'))
