def count_word_occurrences(sentence):
    word_counts = {}

    # Split the sentence into words
    words = sentence.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

input_sentence = input("Enter a sentence: ")
result = count_word_occurrences(input_sentence)
print("Word occurrences:")
print(result)
