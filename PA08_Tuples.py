# PA08 - Tuples
# 06/22/2023

import random

# Create the initial Tuple from a range of integers -100 -> 100
# Testing showed at least a single negative value in each run
tuple_example = tuple(
    (
        (random.randrange(-100, 100), random.randrange(-100, 100)),
        (random.randrange(-100, 100), random.randrange(-100, 100)),
        (random.randrange(-100, 100), random.randrange(-100, 100)),
        (random.randrange(-100, 100), random.randrange(-100, 100)),
        (random.randrange(-100, 100), random.randrange(-100, 100)),
        (random.randrange(-100, 100), random.randrange(-100, 100)),
    )
)
print("input: ", tuple_example)

# Tuples are unchangable so we create a list for staging
staging_list = []

# Loop through the first tuple and split the elements
for first_number, second_number in tuple_example:
    # convert the first set of numbers
    if first_number <= 0:
        first_number_converted = first_number * -1
    else:
        first_number_converted = first_number
    # Convert the second set of numbers
    if second_number >= 0:
        second_number_converted = second_number * -1
    else:
        second_number_converted = second_number

    # Append to the staging area
    staging_list.append((first_number_converted, second_number_converted))

# Build final output tuple from work area
output_tuple = tuple(staging_list)
print("output:", output_tuple)
