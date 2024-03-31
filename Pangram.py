# Check if sentence is a pangram
import string
def is_pangram(str1, alphabet = string.ascii_lowercase ):
    str1 = str1.lower()
    for letter in alphabet:
        if letter not in str1:
            return False
    
    return True

user_input = input("Enter your pangram: ")

print(is_pangram(user_input))
