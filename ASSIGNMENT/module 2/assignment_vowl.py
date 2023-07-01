def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter.lower() in vowels:
        return True
    else:
        return False


letter = input("Enter a letter: ")
if is_vowel(letter):
    print(f"The letter '{letter}' is a vowel.")
else:
    print(f"The letter '{letter}' is not a vowel.")
