# PA04
# 06/19/2023

# Imports standard functionality
import random, statistics
    
# Global Declarations
loop_limiter=21
display_output_list='The list contains: {}'
display_lowest='The lowest random number was: {}'
display_highest='The highest random number was: {}'
display_sum='The total daily sales was: {}'
display_average='The average random number was: {}'
display_over_50= """Random numbers > 50
{}"""

class random_utility:
    
    # Do constructor when instantiated
    def __init__(self, loop_iterations):
        self.loop_iterations=loop_iterations
        pass
    
    # Get the list output based on loop limit
    def get_list_output(self):
        
        # Local variables
        while_exit=False
        while_counter=1
        output_list=[]
        
        # Loop until counter exits
        # We got the loop limit from the constructor
        while while_exit==False:
            # our range allows for int between 1 and 100
            place_holder=random.randrange(1, 100)
            output_list.append(place_holder)
            while_counter += 1
            if while_counter >= self.loop_iterations:
                while_exit = True
                pass
        # Return the output from loop 
        return output_list
    
    def over_50(self,output_result):
        output_over_50=[]
        
        # Get the int's from list over 50
        for number in output_result:
            if number > 50:
                output_over_50.append(number)
                pass  
        return output_over_50

# Instantiate the class and pass value to constructor   
class_reference=random_utility(loop_limiter)

# Call Methods
output_result = class_reference.get_list_output()
output_over_50_result = class_reference.over_50(output_result)

# Format data
minimum=min(output_result)
maximum=max(output_result)
total_value=sum(output_result)
# Floor division keeps the int or fltp input
average=(statistics.mean(output_result))

# Display for the user
print(display_output_list.format(output_result))
print(display_lowest.format(minimum))
print(display_highest.format(maximum))
print(display_sum.format(total_value))
print(display_average.format(average))
print(display_over_50.format(output_over_50_result))