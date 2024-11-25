# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("--+---+--")
    print("\n")

# Function to check if the current player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

# Function to check if the board is full (draw situation)
def is_draw(board):
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize an empty board
    players = ["X", "O"]  # Player X goes first
    turn = 0  # To keep track of whose turn it is

    while True:
        print_board(board)  # Print the board
        current_player = players[turn % 2]  # Determine current player
        print(f"Player {current_player}'s turn")

        # Get player input
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 3 for both row and column.")
            continue

        # Place the player's mark
        board[row][col] = current_player

        # Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        turn += 1

# Run the game
if __name__ == "__main__":
    play_game()
