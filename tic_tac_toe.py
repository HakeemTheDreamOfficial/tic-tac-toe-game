import random as rand

board = ["","","","","","","","",""]
#Prints board in user friendly format
def print_board():
    print(" ")
    print(board[0] +"   | "+ board[1] + " |" + board[2])
    print("----------")
    print(board[3] +"   | "+ board[4] + " |" + board[5])
    print("----------")
    print(board[6] +"   | "+ board[7] + " |" + board[8])

#These are all of the possible winning combinations
winning_combinations = [
    [0, 1, 2], #top row
    [3, 4, 5], #middle row
    [6, 7, 8], #bottom row
    [0, 3, 6], #left column
    [1, 4, 7], #middle column
    [2, 5, 8], #right column
    [0, 4, 8], #diagonal
    [6, 4, 2], #diagonal
    ]

#This variable dictates whether or not a win has been seen for
Win_or_no = "no"

Tie_or_no = "no"

#This function checks for a tie
def check_tie():
    global Tie_or_no
    num_spaces_left = board.count("")
    if num_spaces_left == 0:
        Tie_or_no = "Yes"
        print_board()
        print("Tie Game.")
        print("Game Over")

#This function checks if anyone has won
def check_winner():
    global Win_or_no
    for combination in winning_combinations:
        if (board[combination[0]] == "X" and
            board[combination[1]] == "X" and
            board [combination[2]] == "X"):
            Win_or_no = "Yes"
            print_board()
            print("X has won.")
            print("Game Over")
            break
        elif (board[combination[0]] == "O" and
            board[combination[1]] == "O" and
            board [combination[2]] == "O"):
            Win_or_no = "Yes"
            print_board()
            print("O has won.")
            print("Game Over")
            break

#This path is only for the first turn of X
def player_path_X_first_turn():
    instructions = input('Do you want the instructions? Type "Yes" or "No".')
    if instructions.strip().upper() == ("YES"):
        print("Choose a number going from 1 to 9 to occupy a space.")
        print("Numbers go from left to right and top down.")
        print("Therefore, the top-left square is 1 and the center square is 5.")
    print_board()
    while True:
        chosen_number = input("You choose the square. Please enter a number from 1-9.")
        try:
            chosen_number = int(chosen_number)
            if 1<= chosen_number <=9:
                chosen_number = chosen_number - 1
                if board[chosen_number] == "":
                    board[chosen_number] = "X"
                    print_board()
                    break
                else:
                    chosen_number1 = chosen_number + 1
                    print("Square", chosen_number1, "is occupied.")
            else:
                print("Please enter a valid number from 1-9.")
        except ValueError:
            print("Please enter a valid number.")

#This is the player's path for all turns after the first for O
def player_path_X():
    print_board()
    while True:
        chosen_number = input("You choose the square. Please enter a number from 1-9.")
        try:
            chosen_number = int(chosen_number)
            if 1<= chosen_number <=9:
                chosen_number = chosen_number - 1
                if board[chosen_number] == "":
                    board[chosen_number] = "X"
                    print_board()
                    break
                else:
                    chosen_number1 = chosen_number + 1
                    print("Square", chosen_number1, "is occupied.")
            else:
                print("Please enter a valid number from 1-9.")
        except ValueError:
            print("Please enter a valid number.")

#This is the cpu's path for if the player chooses path X
def cpu_path_X():
    while True:
        cpu_number = rand.randint(0,8)
        if board[cpu_number] == "":
            board[cpu_number] = "O"
            break

#This path is only for the first turn of O
def player_path_O_first_turn():
    instructions = input('Do you want the instructions? Type "Yes" or "No".')
    if instructions.strip().upper() == ("YES"):
        print("Choose a number going from 1 to 9 to occupy a space.")
        print("Numbers go from left to right and top down.")
        print("Therefore, the top-left square is 1 and the center square is 5.")
    print_board()
    while True:
        chosen_number = input("You choose the square. Please enter a number from 1-9.")
        try:
            chosen_number = int(chosen_number)
            if 1<= chosen_number <=9:
                chosen_number = chosen_number - 1
                if board[chosen_number] == "":
                    board[chosen_number] = "O"
                    print_board()
                    break
                else:
                    chosen_number1 = chosen_number + 1
                    print("Square", chosen_number1, "is occupied.")
            else:
                print("Please enter a valid number from 1-9.")
        except ValueError:
            print("Please enter a valid number.")

#This is the player's path for all turns after the first for O
def player_path_O():
    print_board()
    while True:
        chosen_number = input("You choose the square. Please enter a number from 1-9.")
        try:
            chosen_number = int(chosen_number)
            if 1<= chosen_number <=9:
                chosen_number = chosen_number - 1
                if board[chosen_number] == "":
                    board[chosen_number] = "O"
                    print_board()
                    break
                else:
                    chosen_number1 = chosen_number + 1
                    print("Square", chosen_number1, "is occupied.")
            else:
                print("Please enter a valid number from 1-9.")
        except ValueError:
            print("Please enter a valid number.")

#This is the cpu's path for if the player chooses path O
def cpu_path_O():
    while True:
        cpu_number = rand.randint(0,8)
        if board[cpu_number] == "":
            board[cpu_number] = "X"
            break

#This is the entirity of path O
def full_path_O():
    player_path_O_first_turn()
    while True:
        cpu_path_O()
        check_winner()
        if Win_or_no == "Yes":
            break
        check_tie()
        if Tie_or_no == "Yes":
            break
        player_path_O()
        check_winner()
        if Win_or_no == "Yes":
            break
        check_tie()
        if Tie_or_no == "Yes":
            break

#This is the entirity of path X
def full_path_X():
    player_path_X_first_turn()
    while True:
        cpu_path_X()
        check_winner()
        if Win_or_no == "Yes":
            break
        check_tie()
        if Tie_or_no == "Yes":
            break
        player_path_X()
        check_winner()
        if Win_or_no == "Yes":
            break
        check_tie()
        if Tie_or_no == "Yes":
            break


print_board()
while True:
    X_or_O = input("Choose either X or O.")
    if X_or_O.strip().upper() == ("X"):
        full_path_X()
        break
    elif X_or_O.strip().upper() == ("O"):
        full_path_O()
        break
    else:
        print("Please enter a valid letter.")