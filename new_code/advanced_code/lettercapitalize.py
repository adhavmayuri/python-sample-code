def LetterCapitalize(a_string):
    capitalized = a_string.title()
    return capitalized

# Keep this function call here to see how to enter arguments in Python.
# This will take user input and capitalize the first letter of each word.
user_input = input("Enter a string: ")
capitalized_string = LetterCapitalize(user_input)
print(capitalized_string)
