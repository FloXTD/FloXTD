import random


# Function to print a board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--+---+---+---+---+---+--")

# Check for a win
def check_win(board, player):
    row_count = len(board)  # Number of rows
    col_count = len(board[0])  # Number of columns

    # Check for vertical win
    for c in range(col_count):
        for r in range(row_count - 3):  # To ensure there are at least 4 rows below
            if (
                board[r][c] == player and
                board[r+1][c] == player and
                board[r+2][c] == player and
                board[r+3][c] == player):
                return True

    # Check for horizontal win
    for r in range(row_count):
        for c in range(col_count - 3):
            if (
                board[r][c] == player and
                board[r][c+1] == player and
                board[r][c+2] == player and
                board[r][c+3] == player):
                return True

    # Check for diagonal win (top-left to bottom-right)
    for r in range(row_count - 3):
        for c in range(col_count - 3):
            if (
                board[r][c] == player and
                board[r+1][c+1] == player and
                board[r+2][c+2] == player and
                board[r+3][c+3] == player
            ):
                return True

    # Check for diagonal win (bottom-left to top-right)
    for r in range(3, row_count):  # Start from the 4th row to avoid out-of-bounds
        for c in range(col_count - 3):
            if (
                board[r][c] == player and
                board[r-1][c+1] == player and
                board[r-2][c+2] == player and
                board[r-3][c+3] == player
            ):
                return True

    # No win found
    return False


# Function to check if it is a draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)


# Get the move from the player
def get_player_move(board):
    while True:
        try:
            # Get player input
            col = int(input("Enter a column (1-7): ")) - 1

            # Check if input is in the valid range
            if col < 0 or col > 6:
                print("Invalid input! Column must be between 1 and 7.")
                continue

            # Check for the first possible row (starting from the bottom)
            for row in range(5, -1, -1):  # Adjusted to iterate over the 6 rows (0-5)
                if board[row][col] == " ":
                    return row, col  # Return valid position

            # If no empty rows are found
            print("This column is full! Please select another.")

        except ValueError:
            print("Invalid input! Please enter numbers between 1 and 7.")


# To play the game
def play_game():
    board = [[" " for _ in range(7)] for _ in range(6)]  # 6 rows and 7 columns
    turn = 0
    players = ["O", "X"]

    while True:
        print_board(board)
        current_player = players[turn % 2]  # Determines current player

        print(f"Player {current_player}'s turn")
        row, col = get_player_move(board)
        board[row][col] = current_player  # Place mark of current player

        # Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("It is a draw.")
            break

        turn += 1  # Move to the next turn


# Start the game
play_game()
