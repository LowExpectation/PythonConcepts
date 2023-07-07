# Caleb Woods
# PA 18 - Library Book Management
# 07-06-2023

# Global Declarations
welcome_message = True
logic_continue = True
book_list = []

# Class declaration
class library_functions:
     
    def __init__(instance) -> None:
        pass
    
    def __str__(instance) -> str:
        pass
    
    def new_book(instance): # title, author, ISBN, genre
        add_book=[]
               
        # We will give the user the ability to input these values
        book_title = input("Please input the book title: ")
        book_author = input("Please input the book author(s): ")
        book_isbn = input("Please input the book ISBN: ")
        book_genre = input("Please input the book genre: ")
        book_availability = input("Is this book available? Y or N: ")
        book_quantity = input("How many copies of the book are being added?: ")
        
        add_book.append((book_title, book_author, book_isbn, book_genre, book_availability, book_quantity))
        return add_book
    
    def update_book(instance, input_list):
        
        add_return=[]
        message_helper="Current {} is {}. Please enter new value or press enter to keep existing: "
                
        # Display with index for user to select 
        for index, entry in enumerate(input_list, start=0):
            print(index, entry)

        # Get user input
        edit_item = input("Please enter the number of the record to edit: ")
        print()
        
        # Check input is valid and move forward accordingly
        if edit_item.isdigit() == True:
            edit_int = int(edit_item)
            
            # Make this a 2D list by converting to a tuple from the indexed list
            try:
                focused_record = (input_list[edit_int])
            except IndexError:
                edit_int=None
                add_return=[]
                print("Please choose a valid record for editing!")                
                input_holder=input("Please press enter to continue")
                return add_return, edit_int
            
               
            # We will give the user the ability to input these values
            for title, author, isbn, genre, availability, quantity in focused_record:
                    
                # Use the new value or if nothing entered use current value
                # Im not sure how to set a default value on the CLI so we have to post process
                 book_title = input(message_helper.format("Title",title))
                 if book_title == "":
                     book_title = title
                     
                 book_author = input(message_helper.format("Author",author))
                 if book_author == "":
                     book_author = author
                     
                 book_isbn = input(message_helper.format("ISBN",isbn))
                 if book_isbn == "":
                     book_isbn = isbn
                     
                 book_genre = input(message_helper.format("Genre",genre))
                 if book_genre == "":
                     book_genre = genre
                     
                 book_availability = input(message_helper.format("Availability",availability))
                 if book_availability == "":
                     book_availability= availability
                     
                 book_quantity = input(message_helper.format("Quantity",quantity))
                 if book_quantity == "":
                     book_quantity = quantity
        
            add_return.append((book_title, book_author, book_isbn, book_genre, book_availability, book_quantity))
            
        else:
            print("Please enter a numerical input from the rows provided")
            input_holder=input("Please press enter to continue")
            print()
            edit_int=None

        return add_return, edit_int
    
    def remove_book(instance, input_list):
        
        # loop through and display record with true index
        for index, entry in enumerate(input_list, start=0):
            print(index, entry)

        # Get user input from the index
        delete_item = input("Please enter the number of the record to delete: ")
        print()
        
        # Validate the input contains a numeric entry
        if delete_item.isdigit() == True:
            delete_int = int(delete_item)
            return delete_int
        else:
            print("Please enter a numerical input from the rows provided")
            input_holder=input("Please press enter to continue")
            print()
            delete_int= None
            return delete_int
    
        # Display the current result set for user
    def display(instance, input_list):
        
        # If a record exists then we will display it otherwise we print message 
        if len(input_list) == 0:
            print("No records to display")
            input_holder=input("Please press enter to continue")
            print()
        else:
            for index, entry in enumerate(input_list, start=0):
                print(index, entry)
            print()
            output_holder=input("Press Enter to continue")
            print() 
            
    def welcome_message(instance, welcome_header):
        
        welcome_options = """
        1: Add a book
        2: Delete a book
        3: Sort the book list
        4: Edit an existing book
        5: Display current Records
        6: Exit the utility
        
        Entry:"""
        
        # skip the header line when multiple calls
        if welcome_header == True:
            print("Welcome to the library book repository")
            print()
            pass
        print("Please choose an option to proceed")
        print("Type the number of the option and press enter when ready")
        print()
        
        # Give the user the instructions message 
        welcome_selection = input(welcome_options)
        print()
        
        return welcome_selection
    
    # Sort the result set for the user
    def sort(instance, input_list):        
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
                input_holder=input("Please press enter to continue")
                print()
        return sort_result
    
# Create a memory reference to class for instance object
library_reference = library_functions()

# Perform a while loop until exit
# Exit is selected from the input prompt
# we will just call the methods until completion
while logic_continue == True:
    # Welcome one and all!
    welcome_output = library_reference.welcome_message(welcome_message)
    # Set the header message to skip
    welcome_message = False

    # Which option did the user choose
    match welcome_output:
        
        # Add a book
        case "1":
            AddBook_return  = library_reference.new_book()
            book_list.append(AddBook_return)
            print("New book inserted")
            print()
            
        # Delete a book
        case "2":
            if len(book_list) == 0:
                print("No users to delete. Please add a user first")
                input_holder=input("Please press enter to continue")
                print()
            else:
                delete_item = library_reference.remove_book(book_list)
                
                # Validate a valid arguments from the validations
                if delete_item==None:
                    pass
                else:
                    try:
                        del book_list[delete_item]
                    except IndexError:
                        print("Please choose a valid record for deletion")
                        input_holder=input("Please press enter to continue")
                        print()
                                         
        # Sort the book list
        case "3":
            if len(book_list) == 0:
                print("No users to sort. Please add a user first")
                input_holder=input("Please press enter to continue")
                print()
            else:
                # Get a new copy of the sorted output from method
                sort_result = library_reference.sort(book_list)
                book_list = sort_result[:]
        
        # Edit a book entry        
        case "4":
            if len(book_list) == 0:
                print("No users to edit. Please add a user first")
                input_holder=input("Please press enter to continue")
                print()
            else:
                edited_value, edit_index = library_reference.update_book(book_list)
                
                # check returns of our validations before updating
                if edited_value !=[] and edit_index!=None:
                    book_list[edit_index] = edited_value
                else:
                    pass
                
        # Display the current results
        case "5":
            library_reference.display(book_list)            
            
        # Exit the loop       
        case "6":
            logic_continue = False
            print("Goodbye")
            
        # Handle others
        case _:
            print("Please select a valid option")
            input_holder=input("Please press enter to continue")
            print()
    