# PA05
# 06/21/2023

# Global Declarations
welcome_message = True
logic_continue = True
guest_list = []

class wedding_utility:
    # Constructor
    def __init__(self) -> None:
        pass
    
    # Add a user
    def add(self):
        add_guest = []

        # We will give the user the ability to input these values
        # Any user inputs could use more validation than this in real situation
        first_name = input("Please input guest first name: ")
        last_name = input("Please input guest last name: ")
        city = input("Please input guest city of residence: ")
        state = input("Please input guest state of residence: ")
        guest_type = input("Is this the Bride or Grooms guest? Enter B or G: ")
        
        # Append to return list for the values entered
        add_guest.append((first_name, last_name, city, state, guest_type))
        return add_guest

    # delete the value user picks
    def delete(self, input_list):
        
        # loop through and display record with true index
        for index, entry in enumerate(input_list, start=0):
            print(index, entry)

        # Get user input from the index
        delete_item = input("Please enter the number of the record to delete: ")
        print()
        
        # This can break if user enters another value outside of the index shown
        delete_int = int(delete_item)
        return delete_int

    # Sort the result set for the user
    def sort(self, input_list):        
        sort_result = []

        # Build a new table so we can sort in the method
        # Not very performance efficient...
        for entry in input_list:
            sort_result.append(entry)

        # Ask user what sort type is preferred
        print("Sort Ascending or Descending?")
        sort_type = input("Type A or D: ")
        print()

        # Sort based on user input
        match sort_type:
            case "A":
                sort_result.sort()
            case "a":
                sort_result.sort()
            case "D":
                sort_result.sort(reverse=True)
            case "d":
                sort_result.sort(reverse=True)
            case _:
                print("Please select a valid sort option")
                print()
        return sort_result

    # Edit an element of the list
    # only allowing for a whole row to be edited
    def edit(self, input_list):
        
        # Display with index for user to select 
        for index, entry in enumerate(input_list, start=0):
            print(index, entry)

        # Get user input
        edit_item = input("Please enter the number of the record to edit: ")
        print()
        # This should be checked before casting to int or it will dump
        edit_int = int(edit_item)
        # We call this method to allow for the new row to be prepared
        add_return = wedding_utility.add(self)

        return add_return, edit_int

    # Display the display prompt for user
    def welcome_message(self, welcome_header):
        welcome_options = """
        1: Add a guest
        2: Delete a guest
        3: Sort the guest list
        4: Edit an existing guest
        5: Exit the utility
        6: Display Current Records
        
        Entry:"""
        # skip the header line when multiple calls
        # in my mind that would seem cheesy
        if welcome_header == True:
            print("Welcome to the wedding guest list")
            pass
        print("Please choose an option to proceed")
        print("Type the number and press enter when ready")
        welcome_selection = input(welcome_options)
        print()
        # Need to validate the input selection from user
        return welcome_selection

    # Display the current result set for user
    def display(self, input_list):
        
        # If a record exists then we will display it otherwise we print message 
        if len(input_list) == 0:
            print("No records to display")
            print()
        else:
            for index, entry in enumerate(input_list, start=0):
                print(index, entry)
            print()


# We may add logic to the constructor later
wedding_reference = wedding_utility()

# Perform a while loop until exit
# Exit Is selected from the input prompt
# we will just call the methods until completion
while logic_continue == True:
    # Welcome one and all!
    welcome_output = wedding_reference.welcome_message(welcome_message)
    # Set the header message to skip
    welcome_message = False

    # Which option did the user choose
    match welcome_output:
        # Add a guest
        case "1":
            add_return = wedding_reference.add()
            guest_list.append(add_return)
        # Delete a guest
        case "2":
            if len(guest_list) == 0:
                print("No users to delete. Please add a user first")
                print()
            else:
                delete_item = wedding_reference.delete(guest_list)
                # This index should be checked before being offered to the del statement 
                del guest_list[delete_item]
                pass
        # Sort the guest list
        case "3":
            if len(guest_list) == 0:
                print("No users to sort. Please add a user first")
                print()
            else:
                sort_result = wedding_reference.sort(guest_list)
                guest_list = sort_result[:]
        # Edit a guest
        case "4":
            if len(guest_list) == 0:
                print("No users to edit. Please add a user first")
                print()
            else:
                edited_value, edit_index = wedding_reference.edit(guest_list)
                guest_list[edit_index] = edited_value
        # Exit the loop
        case "5":
            logic_continue = False
            print("Goodbye")
        # Display the current results
        case "6":
            wedding_reference.display(guest_list)
        # Handle others
        case _:
            print("Please select a valid option")
