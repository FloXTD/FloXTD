import random

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("--+---+--")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check reverse diagonal
        return True
    return False

# Function to check if the game is a draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm to get the best move
def minimax(board, depth, is_maximizing, alpha, beta):
    # Check for terminal states (win or draw)
    if check_win(board, "O"):
        return 1  # AI wins
    if check_win(board, "X"):
        return -1  # Player wins
    if is_draw(board):
        return 0  # Draw
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  # AI's move
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "  # Undo move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  # Player's move
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "  # Undo move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI
def best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"  # AI's move
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = " "  # Undo move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function for the player's move
def get_player_move(board):
    while True:
        try:
            # Get player input
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            
            # Check if the input is within the valid range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be between 1 and 3.")
                continue

            # Check if the selected cell is already taken
            if board[row][col] != " ":
                print("This cell is already taken! Please choose another.")
                continue
            
            return row, col
        
        except ValueError:
            print("Invalid input! Please enter numbers between 1 and 3.")

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = 0
    
    while True:
        print_board(board)
        
        if turn % 2 == 0:  # Player's turn
            print("Player's turn:")
            row, col = get_player_move(board)
            board[row][col] = "X"
        else:  # AI's turn
            print("AI's turn:")
            row, col = best_move(board)
            board[row][col] = "O"

        # Check for win or draw
        if check_win(board, "X"):
            print_board(board)
            print("Player wins!")
            break
        elif check_win(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1  # Move to the next turn

# Start the game
play_game()
