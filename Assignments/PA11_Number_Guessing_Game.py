# PA11- Number Guessing Game

# The game is simple.
# The user has to guess the randomly generated number that lies between
# the range from 1 to 100. That’s it.

# Is the game that simple?

# Yeah, it is.

# But, there is one thing that we have to provide to the users to guess the number.
# That’s hints. We have to provide a message to the user saying the current
# guessed number is less than the correct number
# or the current guessed number is greater than the correct number.
# So that users will know in which direction they have to go.

# We can make it more exciting by adding extra features like maximum number of chances to guess,
# increasing the range, setting a timer, etc..,

# Creating the basic working game is mandatory.
# After it, we can add more features as discussed.
# So, we are going to create the basic version of the game in this section.
# And then we will move to add new features.

# I want you to try creating the game without blindly copying the code.
# So, I am going to explain the algorithm first.
# It will help you to code yourself or understand the code quickly.

# Let’s see the algorithm to create the Number guessing game.
# Algorithm

# Make sure you understand the algorithm before moving to the coding part.

# Define the range of the numbers. By default, it’s 1-100 but you can change it as you prefer.
# Generate a random integer from the above range (1-100).
# Start the game by displaying the user a message saying “Guess the number from X to Y”.
# You may update the message as you wish.
# Initialize a variable to 0 to count the total number of
# chances that the user has taken to guess the number correctly.
# Write an infinite loop.
# Ask the user to guess the number.
# If the current guessed number is equal to the randomly generated number,
# then congratulate the user with a message as you like.
# An example would be “-> Hurray! You got it in 5 steps!”.
# Break the loop after congratulating the user.
# If the current guessed number is less than the randomly generated number,
# then give a message to the user saying “-> Your number is less than the random number”
# or a custom message having the same meaning.
# If the current guessed number is greater than the randomly generated number,
# then give a message to the user saying “-> Your number is greater than the random number”
# or a custom with the same meaning.
# Finally, increment the chances that the user has taken to guess.

# You would have got code in your mind after seeing the algorithm.
# Don’t worry even if you don’t get the complete code.
# But, make sure you understand the above algorithm.

# This is a fun project when it's finished. Give it your best shot.
# Don't loose a lot of sleep if you struggle.
# Go back to the lessons in this Module and previous Modules for all the code needed.

# There are some things that you might want to look at as ideas.

# The range is defined inside the __init__ method so that it can be used across the class methods.
# We can easily change it in one place that changes across the app accordingly.
# There is a separate method to generate the random number which follows
# the principle of “separate the concerns”. Here, our method has little code,
# but it might increase in the future.
# Finally, we have used class so that every method that’s related to the game will reside inside it.
# And it can be easily reused in some other apps.

# All the points that are discussed above are related to writing clean code.
# We all should try to write clean code including appropriate comments that
# help others understand what and why you added each significant code block to your solution.

# The output of the game should look as follows.

# $ python number_guessing_game.py
# Guess the randomly generated number from 1 to 100
# Enter the guessed number: 50
# -> Your number is less than the random number
# Enter the guessed number: 75
# -> Your number is less than the random number
# Enter the guessed number: 90
# -> Your number is greater than the random number
# Enter the guessed number: 85
# -> Your number is greater than the random number
# Enter the guessed number: 80
# -> Hurray! You got it in 5 steps!


# Save the program in a file named guessing_game.py
# and attach that guessing_game.py file to this assignment.
# Add the required comments to top of your .py file:

# Include comments in your code following industry standards.
# Not including comments in your code or
# random comments that do not pertain to your code will result in
# points being deducted.
# Comments inside code are a requirement for most software development businesses.

# Caleb Woods
# PA11 - Number Guessing Game
# 07-16-2023

import random

class number_guessing:
    # Constructor set some class values for use later
    def __init__(instance) -> None:
        instance.random_number = random.randrange(1, 100, 1)
        instance.press_enter = "Please press enter to continue"
        instance.input_guess = 0
        instance.number_of_guesses = 0

    # May be used in the future
    def __str__(instance) -> str:
        pass

    # May be used in the future
    def __repr__(instance) -> str:
        pass

    # Guides the while loop
    def guess_helper(instance) -> bool:
        if int(instance.input_guess) != instance.random_number:
            return True
        else:
            return False

    # Collects the guess and validates it
    def user_guess(instance) -> bool:
        instance.input_guess = input("Please input your guess: ")
        # The order of these validations is important
        while (
            not instance.input_guess.isdigit()
            or instance.input_guess.isspace()
            or int(instance.input_guess) > 100
            or int(instance.input_guess) < 1
        ):
            print()
            instance.input_guess = input(
                "Please pick a valid number between 1 and 100: "
            )

    # Display the game welcome message
    def welcome_message(instance) -> None:
        print()
        print(
            """
        ***** N u m b e r  G u e s s i n g  G a m e *****
        
        A random number between 1 and 100 will be generated
        To play, please try to guess the random number.
        If you do not guess correctly you will be given hints.
        If you do guess correctly, you win the game! """
        )
        print()
        input_holder = input(instance.press_enter)

    # Give hints on the guessed number
    def analyze_answer(instance) -> None:
        # Set the incrementation of the guess number
        instance.number_of_guesses += 1
        
        if int(instance.input_guess) < instance.random_number:
            print("Your number", instance.input_guess, "is less than the random number")
        elif int(instance.input_guess) > instance.random_number:
            print("Your number",instance.input_guess,"is greater than the random number")
        else:
            print("You guessed the correct number in", instance.number_of_guesses,"steps. Congratulations!")
            print()


# Create an instance of the class
ngg_ref = number_guessing()

# Show the welcome prompt
ngg_ref.welcome_message()

# While guess is not equal to hidden number
while ngg_ref.guess_helper():
    # Get the user guess and give hints
    ngg_ref.user_guess()
    ngg_ref.analyze_answer()
