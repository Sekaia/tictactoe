import random
# --------- Global Variables -----------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# Do the players want to keep playing?
want_to_play = True

# If game is still going
game_still_going = True

# Who won
winner = None

# Who's turn is it
current_player = "X"

#resets the game board and winner
def reset_game():
    #global vars
    global board
    global game_still_going
    global current_player
    global winner

    players = ["X", "O"]

    #reset the global variables
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-", ]
    game_still_going = True
    #winner goes first
    if winner != None:
        current_player = winner
    else:
        current_player = random.choice(players)
    winner = None


# display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play a game of tic tac toe
def play_game():
    # Display initial board
    display_board()

    # while the game is ongoing
    while game_still_going:
        # handle a single turn of the current player
        handle_turn(current_player)

        # has the game ended?
        check_if_game_over()

        # change from X to O
        flip_player()


    # game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# handle a single turn of a player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    #check for a valid input
    valid = False
    while not valid:
        #if input is not a number between 1 and 9
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        # if the spot is taken
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()


# is the game over?
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# was there a winner?
def check_for_winner():
    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diag_winner = check_diags()

    #if there is a winner in one of the rows, the winner is declared
    if row_winner:
       winner = row_winner
    # if there is a winner in one of the columns, the winner is declared
    elif column_winner:
        winner = column_winner
    # if there is a winner in one of the diagonals, the winner is declared
    elif diag_winner:
        winner = diag_winner
    #tie
    else:
        #there was no win
        winner = None
    return


# check the rows for a winner
def check_rows():
    # set up global variables
    global game_still_going

    #check if any rows have the same value and isnt a "-"
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # if any row has a match, flag a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# check the columns for a winner
def check_columns():
    # set up global variables
    global game_still_going

    # check if any columnss have the same value and isnt a "-"
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    # if any column has a match, flag a win
    if col_1 or col_2 or col_3:
        game_still_going = False

    # return the winner
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


# check the diagonals for a winner
def check_diags():
    # set up global variables
    global game_still_going

    # check if any diagonals have the same value and isnt a "-"
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    # if any diagonals has a match, flag a win
    if diag_1 or diag_2:
        game_still_going = False

    # return the winner
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


# was it a tie?
def check_if_tie():
    #global var
    global game_still_going

    #if all the spots are taken and a winner hasn't been declared
    if "-" not in board:
        #stop the game
        game_still_going = False
    return


# change players
def flip_player():
    #global var
    global current_player

    # if current player is x, change to o
    if current_player == "X":
        current_player = "O"

    # if current player is o, change to x
    elif current_player == "O":
        current_player = "X"
    return


while want_to_play:
    play_game()

    valid = False
    while not valid:
        keep_playing = input("Do you want to play again? (y/n) ")
        if keep_playing.lower() == "n" or keep_playing.lower() == "no":
            valid = True
            want_to_play = False
        elif keep_playing.lower() == "y" or keep_playing.lower() == "yes":
            valid = True
            reset_game()
        else:
            print("Invalid input.")