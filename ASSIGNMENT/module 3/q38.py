def check_palindrome(string):
    
    string = string.lower().replace(" ", "")

    
    if string == string[::-1]:
        return True
    else:
        return False


input_str = "Madam"
is_palindrome = check_palindrome(input_str)
print(f"The string '{input_str}' is a palindrome: {is_palindrome}")
