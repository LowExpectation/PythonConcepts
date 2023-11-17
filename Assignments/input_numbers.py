# Input Numbers
# input_numbers.py

import os


class input_output:
    # Class global values
    file_list = []

    def __str__(self) -> str:
        # This allows for the rules to be printed easily
        return self.output_rules

    def __init__(self) -> None:
        # This will allow for the user to be explained the rules
        explain_rules = """
        Welcome {}. In this application, you will be prompted to enter integer based values.
        Any values entered besides integers will not be valid and you will be prompted to
        correct your answers. Each input will be saved in a list array and will written to a text
        file named numbers.txt in this current directory.
        
        Press enter to continue: """

        self.output_rules = explain_rules.format(os.getlogin())

        rules_holder = input(self.output_rules)

    def __repr__(self) -> str:
        # Can be used for additional string requirements
        pass

    def prompt_input(self) -> int:
        user_prompt = """
        Please enter an integer for the file: """

        # This will handle the user interaction for gathering integer
        while True:
            try:
                user_input = int(input(user_prompt))
            except ValueError:
                print()
                print("Invalid entries, please try again")
                print()
                continue
            else:
                return user_input

    def continue_loop(self) -> bool:
        valid_yes = ["yes", "y"]
        valid_no = ["no", "n"]

        user_prompt = """
        Do you wish to continue adding integers? Please enter Yes/No: """
        user_input = input(user_prompt)

        # We validate using list range and return will break the loop
        while True:
            if user_input.lower() in valid_yes:
                return True
            elif user_input.lower() in valid_no:
                return False
            else:
                print()
                print("Please enter yes or no to continue")
                print()
                user_input = input(user_prompt)

    def collect_integers(self, user_input) -> None:
        self.file_list.append(user_input)

    def output_text_file(self) -> str:
        # Get current directory and join filename dynamically
        current_directory = os.getcwd()
        output_directory = os.path.join(current_directory, "numbers.txt")
        output_file = open(output_directory, "w")
        # loop and split the integers into file lines
        for integer in self.file_list:
            output_file.write("%s\n" % str(integer))
        # Close and the file for editing
        output_file.close()
        # validate and return results
        if os.path.exists(output_directory):
            return_message = "file saved in " + output_directory
            return return_message
        else:
            return_message = "file could not be saved, an error occured"
            return return_message


# Instantiate the local object and print welcome message
lo_io = input_output()

# Continue prompting user for integer interaction
while True:
    # Get input and validate
    user_input = lo_io.prompt_input()
    # Add the input to file list managed in class
    lo_io.collect_integers(user_input)
    # prompt user to continue the interaction
    continue_loop = lo_io.continue_loop()
    if continue_loop == True:
        continue
    else:
        break

# Have the class generate the file in current directory and output results to cli
return_message = lo_io.output_text_file()
print()
print(return_message)
