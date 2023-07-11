# PA10- Tic-Tac-Toe

# OK, you're going to build your first game using Python Dictionaries.
# For the record, this will probably not be a program you get wealthy from,
# but it could be a start.

# This project incorporates much of what you've learned already in this semester.
# In addition to working with Dictionaries, you'll add conditional logic and
# list elements to your code.

# This matrix is your typical Tic-Tac-Toe game structure -
# three rows (1,2,3) and three columns (A,B,C). The game then has nine cells in the matrix.

# 1A | 1B | 1C

# 2A | 2B | 2C

# 3A | 3B | 3C

# Each cell in the matrix represents a Dictionary Key.
# Each Key will contain a value of "None" to begin the game.
# There will be two people playing the game.
# Each player will be asked to enter his or her first name before the game begins.
# The program will designate the player whose first name has the least number -
# of characters as the first to place an "X" in a matrix cell.
# The other play follows placing an "O" in their first cell.

# You will receive all 50 points for this project if your program enables -
# the two users to fill each cell and exit the program when all cells have -
# a value other than None.

# BONUS! You'll receive another 25 points if your program -
# identifies the person who has won the game by getting three of their Xs or Os in a row.

# Save the program in a file named Tic_Tac_Toe.py and -
# attach that Tic_Tac_Toe.py file to this assignment.

# Add the required comments to top of your .py file:

# Include comments in your code following industry standards.
# Not including comments in your code or random comments that do
# not pertain to your code will result in points being deducted.
# Comments inside code are a requirement for most software development businesses.

# Caleb Woods
# PA 10 - Tic-Tac-Toe
# 07-16-2023


class tic_tak_toe:
    def __init__(instance) -> None:
        # Print the header
        print()
        print("*****T i c  T a c  T o e*****")
        print()

        # Gameboard Dictionary initialize
        instance.gameboard_dictionary = dict(
            {
                "1": None,
                "2": None,
                "3": None,
                "4": None,
                "5": None,
                "6": None,
                "7": None,
                "8": None,
                "9": None,
            }
        )

    def __str__(instance) -> str:
        # Make it easy to print the gameboard
        output = """
        | {} | {} | {} |
        
        | {} | {} | {} |
        
        | {} | {} | {} | """

        return output.format(
            instance.gameboard_dictionary["1"],  # "1A"],
            instance.gameboard_dictionary["2"],  # "1B"],
            instance.gameboard_dictionary["3"],  # "1C"],
            instance.gameboard_dictionary["4"],  # "2A"],
            instance.gameboard_dictionary["5"],  # "2B"],
            instance.gameboard_dictionary["6"],  # "2C"],
            instance.gameboard_dictionary["7"],  # "3A"],
            instance.gameboard_dictionary["8"],  # "3B"],
            instance.gameboard_dictionary["9"],  # "3C"],
        )

    def __repr__(self) -> str:
        # Maybe putting a scordboard in here in the future?
        pass

    def players(instance):
        # Get inputs for players
        instance.player1 = input("Please enter player 1 name: ")
        instance.player2 = input("Please enter player 2 name: ")

        # Do validations P1
        if instance.player1 == "":
            while instance.player1 == "":
                print("Player 1 name must not be blank.")
                instance.player1 = input("Please enter player 1 name: ")

        # Do validations P2
        if instance.player2 == "":
            while instance.player2 == "":
                print("Player 2 name must not be blank.")
                instance.player2 = input("Please enter player 2 name: ")

    def play_order(instance):
        # Check p1 length against p2
        # If equal or greater than, the else will occur
        # X goes first, O goes second
        if len(instance.player1) < len(instance.player2):
            instance.p1_symbol = "X"
            instance.p2_symbol = "O"
            # Set the current turn
            instance.current_turn = "p1"
        else:
            instance.p1_symbol = "O"
            instance.p2_symbol = "X"
            instance.current_turn = "p2"

    def is_board_full(instance):
        # Create a Bool variable
        board_not_full = False

        # Set bool to True if a None exists in the dictionary
        for key, square in instance.gameboard_dictionary.items():
            if square == None:
                board_not_full = True

        return board_not_full

    def fill_board(instance):
        pick_helper = "{}, please pick a square 1-9, left to right"
        # Get player turn and set the next turn
        if instance.current_turn == "p1":
            player = instance.player1
            symbol = instance.p1_symbol
            instance.current_turn = "p2"
        else:
            player = instance.player2
            symbol = instance.p2_symbol
            instance.current_turn = "p1"

        # add a value to the board and validate
        print()
        print(pick_helper.format(player))
        selected_square = input("Square number: ")

        # Check digit, and range values
        while (
            not selected_square.isdigit()
            or int(selected_square) < 1
            or int(selected_square) > 9
            or instance.gameboard_dictionary[selected_square] != None
        ):
            print()
            print("Please pick a valid square")
            print(pick_helper.format(player))
            selected_square = input("Square number: ")
        else:
            instance.gameboard_dictionary[selected_square] = symbol

    def check_board(instance):
        # Check horizontal P1 winning condition
        if (
            (
                instance.gameboard_dictionary["1"] == instance.p1_symbol
                and instance.gameboard_dictionary["2"] == instance.p1_symbol
                and instance.gameboard_dictionary["3"] == instance.p1_symbol
            )
            or (
                instance.gameboard_dictionary["4"] == instance.p1_symbol
                and instance.gameboard_dictionary["5"] == instance.p1_symbol
                and instance.gameboard_dictionary["6"] == instance.p1_symbol
            )
            or (
                instance.gameboard_dictionary["7"] == instance.p1_symbol
                and instance.gameboard_dictionary["8"] == instance.p1_symbol
                and instance.gameboard_dictionary["9"] == instance.p1_symbol
            )
        ):
            instance.winning_player = instance.player1
            return True

        # Check Vertical P1 Winning Condition
        if (
            (
                instance.gameboard_dictionary["1"] == instance.p1_symbol
                and instance.gameboard_dictionary["4"] == instance.p1_symbol
                and instance.gameboard_dictionary["7"] == instance.p1_symbol
            )
            or (
                instance.gameboard_dictionary["2"] == instance.p1_symbol
                and instance.gameboard_dictionary["5"] == instance.p1_symbol
                and instance.gameboard_dictionary["8"] == instance.p1_symbol
            )
            or (
                instance.gameboard_dictionary["3"] == instance.p1_symbol
                and instance.gameboard_dictionary["6"] == instance.p1_symbol
                and instance.gameboard_dictionary["9"] == instance.p1_symbol
            )
        ):
            instance.winning_player = instance.player1
            return True

            # Check diagonal P1 winning condition
        if (
            instance.gameboard_dictionary["1"] == instance.p1_symbol
            and instance.gameboard_dictionary["5"] == instance.p1_symbol
            and instance.gameboard_dictionary["9"] == instance.p1_symbol
        ) or (
            instance.gameboard_dictionary["3"] == instance.p1_symbol
            and instance.gameboard_dictionary["5"] == instance.p1_symbol
            and instance.gameboard_dictionary["7"] == instance.p1_symbol
        ):
            instance.winning_player = instance.player1
            return True

            # Check horizontal P2 winning condition
        if (
            (
                instance.gameboard_dictionary["1"] == instance.p2_symbol
                and instance.gameboard_dictionary["2"] == instance.p2_symbol
                and instance.gameboard_dictionary["3"] == instance.p2_symbol
            )
            or (
                instance.gameboard_dictionary["4"] == instance.p2_symbol
                and instance.gameboard_dictionary["5"] == instance.p2_symbol
                and instance.gameboard_dictionary["6"] == instance.p2_symbol
            )
            or (
                instance.gameboard_dictionary["7"] == instance.p2_symbol
                and instance.gameboard_dictionary["8"] == instance.p2_symbol
                and instance.gameboard_dictionary["9"] == instance.p2_symbol
            )
        ):
            instance.winning_player = instance.player1
            return True

        # Check Vertical P2 Winning Condition
        if (
            (
                instance.gameboard_dictionary["1"] == instance.p2_symbol
                and instance.gameboard_dictionary["4"] == instance.p2_symbol
                and instance.gameboard_dictionary["7"] == instance.p2_symbol
            )
            or (
                instance.gameboard_dictionary["2"] == instance.p2_symbol
                and instance.gameboard_dictionary["5"] == instance.p2_symbol
                and instance.gameboard_dictionary["8"] == instance.p2_symbol
            )
            or (
                instance.gameboard_dictionary["3"] == instance.p2_symbol
                and instance.gameboard_dictionary["6"] == instance.p2_symbol
                and instance.gameboard_dictionary["9"] == instance.p2_symbol
            )
        ):
            instance.winning_player = instance.player1
            return True

            # Check diagonal P2 winning condition
        if (
            instance.gameboard_dictionary["1"] == instance.p2_symbol
            and instance.gameboard_dictionary["5"] == instance.p2_symbol
            and instance.gameboard_dictionary["9"] == instance.p2_symbol
        ) or (
            instance.gameboard_dictionary["3"] == instance.p2_symbol
            and instance.gameboard_dictionary["5"] == instance.p2_symbol
            and instance.gameboard_dictionary["7"] == instance.p2_symbol
        ):
            instance.winning_player = instance.player1
            return True


# Instantiate object
ttt_ref = tic_tak_toe()

# Get player names
ttt_ref.players()

# Set the player symbol and order
ttt_ref.play_order()

while ttt_ref.is_board_full():
    print(str(ttt_ref))

    ttt_ref.fill_board()
    # check for full board and or winner status
    if ttt_ref.check_board():
        print()
        print(ttt_ref.winning_player, "is Victorious!")
        print(str(ttt_ref))
        break
# When board is full but no winner then its a tie
else:
    print(ttt_ref.player1, "and", ttt_ref.player2, "tied")
