# Caleb Woods
# PA 14 - User Input
# 07-16-2023

# Data declarations
validate_message = "Please enter a word with at least four characters"
prompt_message = "Please enter the {} word: "

# Print instructions
print(
    """
You will be asked to enter three words below.
The words must contain at least four characters"""
)
print()

# Get the first word and validate
word1 = input(prompt_message.format("first"))
while len(word1) < 4:
    print()
    print(validate_message)
    word1 = input(prompt_message.format("first"))
# Get the second word and validate
word2 = input(prompt_message.format("second"))
while len(word2) < 4:
    print()
    print(validate_message)
    word2 = input(prompt_message.format("second"))
# Get the third word and validate
word3 = input(prompt_message.format("third"))
while len(word3) < 4:
    print()
    print(validate_message)
    word3 = input(prompt_message.format("third"))

# Slice the strings into an output
# The program should combine the first 3 letters of the first word
# with the last 2 letters of the second word
# and the first letter of the third word into a variable
combined = word1[0:3:1] + word2[-2:] + word3[0:1:1]
print(combined)
