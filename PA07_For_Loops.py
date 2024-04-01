# PA07- Python For Loop
# 07/03/2023

# Loop at outer number and append line until range is satisfied
# Range starts at 0, stops at index 5, and steps +1 
# counts 0 -> 4
for outer_number in range(0,5,1):
    for inner_number in range(0, outer_number + 1):
        # we append the line and use carriage return to build our structure
        print("*", end=' ')
    print("\r")

# Range starts at where we ended in first loop, stops at index 0, and steps -1 
# counts 5 -> 1
for outer_number in range(5,0,-1):
    for inner_number in range(0, outer_number - 1):
        print("*", end=' ')
    print("\r")