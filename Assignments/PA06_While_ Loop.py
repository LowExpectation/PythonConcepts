# Caleb Woods
# PA06- Python While Loop
# 07/03/2023

i = 0
a = "MaricopaCommunityColleges"

while i == 0:
    for letter in a:
        if letter == "u" or letter == "o":
            continue
        else:
            print(letter)
    i += 1
