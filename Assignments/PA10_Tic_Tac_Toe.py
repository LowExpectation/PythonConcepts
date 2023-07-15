# Caleb Woods
# PA 10 - Tic-Tac-Toe
# 07-16-2023

class tic_tak_toe:
    def __init__(instance) -> None:
        # Print the header
        print()
        print(
            """
          ___                 ___  
         (o o)               (o o) 
        (  V  ) Tic Tak Toe (  V  )
        --m-m-----------------m-m--
        """
        )
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
            instance.gameboard_dictionary["1"],
            instance.gameboard_dictionary["2"],
            instance.gameboard_dictionary["3"],
            instance.gameboard_dictionary["4"],
            instance.gameboard_dictionary["5"],
            instance.gameboard_dictionary["6"],
            instance.gameboard_dictionary["7"],
            instance.gameboard_dictionary["8"],
            instance.gameboard_dictionary["9"],
        )

    def __repr__(self) -> str:
        # Maybe putting a scordboard in here in the future?
        pass

    def players(instance) -> None:
        # Get inputs for players
        print()
        instance.player1 = input("Please enter player 1 name: ")
        # Do validations P1
        while instance.player1 == "" or instance.player1.isspace():
            print()
            print("Player 1 name must not be blank.")
            instance.player1 = input("Please enter player 1 name: ")

        print()
        instance.player2 = input("Please enter player 2 name: ")
        # Do validations P2
        while instance.player2 == "" or instance.player2.isspace():
            print()
            print("Player 2 name must not be blank.")
            instance.player2 = input("Please enter player 2 name: ")

    def play_order(instance) -> None:
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

    def is_board_full(instance) -> bool:
        # Create a Bool variable
        board_not_full = False

        # Set bool to True if a None exists in the dictionary
        for key, square in instance.gameboard_dictionary.items():
            if square == None:
                board_not_full = True

        return board_not_full

    def fill_board(instance) -> None:
        pick_helper = "{} ({}), please pick a square 1-9, left to right"
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
        print(pick_helper.format(player, symbol))
        selected_square = input("Square number: ")

        # Check digit, and range values
        while (
            not selected_square.isdigit()
            or selected_square.isspace()
            or int(selected_square) < 1
            or int(selected_square) > 9
            or instance.gameboard_dictionary[selected_square] != None
        ):
            print()
            print("Please pick a valid square")
            print(pick_helper.format(player, symbol))
            selected_square = input("Square number: ")
        else:
            instance.gameboard_dictionary[selected_square] = symbol

    def check_board(instance) -> bool:
        # Check players entries to see if game should continue or win status occured
        if tic_tak_toe.check_horizontal(instance, instance.p1_symbol, instance.player1):
            return True
        if tic_tak_toe.check_vertical(instance, instance.p1_symbol, instance.player1):
            return True
        if tic_tak_toe.check_diagonal(instance, instance.p1_symbol, instance.player1):
            return True
        if tic_tak_toe.check_horizontal(instance, instance.p2_symbol, instance.player2):
            return True
        if tic_tak_toe.check_vertical(instance, instance.p2_symbol, instance.player2):
            return True
        if tic_tak_toe.check_diagonal(instance, instance.p2_symbol, instance.player2):
            return True

    def check_horizontal(instance, symbol, *player) -> bool:
        # Check horizontal P2 winning condition
        if (
            (
                instance.gameboard_dictionary["1"] == symbol
                and instance.gameboard_dictionary["2"] == symbol
                and instance.gameboard_dictionary["3"] == symbol
            )
            or (
                instance.gameboard_dictionary["4"] == symbol
                and instance.gameboard_dictionary["5"] == symbol
                and instance.gameboard_dictionary["6"] == symbol
            )
            or (
                instance.gameboard_dictionary["7"] == symbol
                and instance.gameboard_dictionary["8"] == symbol
                and instance.gameboard_dictionary["9"] == symbol
            )
        ):
            instance.winning_player = "".join(player)
            return True

    def check_vertical(instance, symbol, *player) -> bool:
        # Check Vertical P1 Winning Condition
        if (
            (
                instance.gameboard_dictionary["1"] == symbol
                and instance.gameboard_dictionary["4"] == symbol
                and instance.gameboard_dictionary["7"] == symbol
            )
            or (
                instance.gameboard_dictionary["2"] == symbol
                and instance.gameboard_dictionary["5"] == symbol
                and instance.gameboard_dictionary["8"] == symbol
            )
            or (
                instance.gameboard_dictionary["3"] == symbol
                and instance.gameboard_dictionary["6"] == symbol
                and instance.gameboard_dictionary["9"] == symbol
            )
        ):
            instance.winning_player = "".join(player)
            return True

    def check_diagonal(instance, symbol, *player) -> bool:
        # Check diagonal P1 winning condition
        if (
            instance.gameboard_dictionary["1"] == symbol
            and instance.gameboard_dictionary["5"] == symbol
            and instance.gameboard_dictionary["9"] == symbol
        ) or (
            instance.gameboard_dictionary["3"] == symbol
            and instance.gameboard_dictionary["5"] == symbol
            and instance.gameboard_dictionary["7"] == symbol
        ):
            instance.winning_player = "".join(player)
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
    print(str(ttt_ref))
    print()
    print(ttt_ref.player1, "and", ttt_ref.player2, "tied!")
