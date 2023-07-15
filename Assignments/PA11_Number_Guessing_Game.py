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
