# Caleb Woods
# PA03: Convert Temperatures to and from Celsius, Fahrenheit.
# 07/03/2023

# Set global variables
temperature_display="""
(1) Fahrenheit
(2) Celsius"""
output_helper="{}{} was converted to {}{}"

# Print Welcome splash
print("Please select type the number next to the temperature to be converted and press enter")
print(temperature_display)
print()

selected_temperature = input("Selection: ")

# Depending on user input we will do requested conversion   
match selected_temperature:
    
    case "1": # Fahrenheit -> Celsius
        fahrenheit_input = input("Please enter your Fahrenheit value to be converted: ")
        
        # Validate we have a value that can be worked with
        # If yes then do calculation and output results
        if fahrenheit_input.isdigit() == True:
            celsius_output = (( 5/9 ) * ( int(fahrenheit_input) - 32 ))
            print(output_helper.format(fahrenheit_input,"°F", celsius_output,"°C")) 
        else:
           print("Please enter a numerical input only")
       
    case "2": # Celsius -> Fahrenheit
        celsius_input = input("Please enter your celsius value to be converted: ")
        
        if celsius_input.isdigit() == True:
            fahrenheit_output = (( int(celsius_input) * 1.8 ) +32 )
            print(output_helper.format(celsius_input,"°C", fahrenheit_output,"°F"))
        else:
           print("Please enter a numerical input only")
       
    case _: # Handle all other inputs
        print("Please select a valid option")