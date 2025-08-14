# a. Write a Python program to reverse a string
string = input("Enter a string to reverse: ")
print("Reversed string:", string[::-1])

# b. Write a Python program to check if a string is a palindrome
string = input("Enter a string to check palindrome: ")
print("Is palindrome:", string == string[::-1])

# c. Write a Python program to check if a string contains only digits
string = input("Enter a string to check digits: ")
print("Contains only digits:", string.isdigit())

# d. Write a Python program to find the longest word in a sentence
sentence = input("Enter a sentence to find longest word: ")
words = sentence.split()
print("Longest word:", max(words, key=len))

# e. Write a Python program to find the length of the last word in a sentence
sentence = input("Enter a sentence to find length of last word: ")
words = sentence.split()
print("Length of last word:", len(words[-1]))
