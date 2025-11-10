import os
import sys 

# --- Configuration ---
BOARD_SIZE = 3
EMPTY_CELL = ' '

# --- Utility Functions ---

def create_board():
    """Initializes and returns an empty 3x3 Tic-Tac-Toe board."""
    return [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def clear_screen():
    """Clears the console screen for better board visualization."""
    # Command for Windows is 'cls', for Linux/macOS is 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    """Prints the current state of the board in a visually clear 3x3 grid format."""
    
    # 1. Column Header (Aligned with cells: 0 | 1 | 2)
    header_numbers = " | ".join(str(i) for i in range(BOARD_SIZE))
    print("\n    " + header_numbers)
    
    # Determine the length of the separator line for alignment
    SEPARATOR_LENGTH = BOARD_SIZE * 4 + 1 
    
    # 2. Print Separator Line
    print("  " + "-" * SEPARATOR_LENGTH) 
    
    # 3. Print Rows
    for i, row in enumerate(board):
        # Print the row content (e.g., 0 | X |   | O |)
        print(f"{i} | {' | '.join(row)} |")
        # Print the separator line after the row
        print("  " + "-" * SEPARATOR_LENGTH)

    print() # Final newline for spacing

def player_input(player, board):
    """
    Prompts the player for a move and ensures the move is valid (in bounds and empty).
    Includes robust error handling for non-integer and empty input.
    """
    valid_move = False
    
    while not valid_move:
        print(f"Player {player}'s turn.")
        try:
            # Read input as strings first to handle empty input gracefully
            row_str = input(f"Enter row (0 , 1 or 2): ")
            col_str = input(f"Enter column ((0 , 1 or 2)): ")
            
            if not row_str or not col_str:
                print("❌ Input cannot be empty. Try again.")
                continue

            # Attempt conversion to integer
            row = int(row_str)
            col = int(col_str)

            # Validation Checks
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                if board[row][col] == EMPTY_CELL:
                    valid_move = True
                    return row, col
                else:
                    print("🚫 That cell is already taken! Please choose an empty cell.")
            else:
                print(f"❌ Input out of bounds. Row and column must be between 0 and {BOARD_SIZE-1}.")

        except ValueError:
            print("⚠️ Invalid input. Please enter a whole number (0, 1, or 2).")
            
def check_win(board, player):
    """Checks if the given player has three symbols in a row, column, or diagonal."""
    def check_line(line):
        return all(cell == player for cell in line)

    # Check Rows
    for row in board:
        if check_line(row): return True
    
    # Check Columns
    for col in range(BOARD_SIZE):
        if check_line([board[row][col] for row in range(BOARD_SIZE)]): return True

    # Check Diagonals
    if check_line([board[i][i] for i in range(BOARD_SIZE)]): return True # Main diagonal
    if check_line([board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)]): return True # Anti-diagonal
    
    return False

def check_tie(board):
    """Checks if the board is full (no empty cells remaining)."""
    for row in board:
        if EMPTY_CELL in row:
            return False
    return True
            
def show_rules():
    """Prints the rules and instructions for Tic-Tac-Toe."""
    print("\n" + "="*40)
    print("         TIC-TAC-TOE RULES")
    print("="*40)
    print("* The board is a 3x3 grid.")
    print("* Two players take turns marking a cell with their symbol (X or O).")
    print("* The goal is to get three of your symbols in a row.")
    print("* The board is accessed using **Row** and **Column** indices (0, 1, or 2).")
    print("="*40 + "\n")

def get_player_choice():
    """Asks Player 1 to choose X or O and sets up the player order."""
    choice = ''
    while choice.upper() not in ('X', 'O'):
        choice = input("Player 1: Do you want to be X or O? ").upper()
        
    player1_symbol = choice
    player2_symbol = 'O' if player1_symbol == 'X' else 'X'
    
    print(f"Player 1 is **{player1_symbol}** and Player 2 is **{player2_symbol}**.")
    # Return the list [First Player, Second Player]
    return [player1_symbol, player2_symbol] 

# --- Step 6: The Main Game Loop (play) ---

def play():
    """Manages the entire game flow."""
    
    clear_screen()
    print("✨ Welcome to TIC TAC TOE! ✨")
    
    # 1. Show Rules and Board Example
    show_rules()
    
    # 2. Get Player Symbol Choice
    players_in_order = get_player_choice() 
    
    # Initialization
    board = create_board()
    current_player_index = 0
    winner = None
    
    # Game Loop
    while winner is None and not check_tie(board):
        
        current_player = players_in_order[current_player_index]
        
        # Clear the screen before showing the updated board
        clear_screen()
        print(f"--- TIC TAC TOE (Player {current_player}'s Turn) ---")
        
        # a. Display the board
        display_board(board)
        
        # b. Get input, c. Update board
        row, col = player_input(current_player, board)
        board[row][col] = current_player
        
        # d. Check for a winner
        if check_win(board, current_player):
            winner = current_player
            break
        
        # e. Check for a tie
        if check_tie(board):
            break

        # f. Switch to the next player
        current_player_index = 1 - current_player_index 
        
    # --- Final Result ---
    clear_screen()
    print("\n--- GAME OVER ---")
    display_board(board)
    
    if winner:
        print(f"🥳 **Player {winner} wins!** Congratulations!")
    else:
        print("🤝 **It's a Tie!** No winner this round.")

# Run the game
if __name__ == "__main__":
    play()