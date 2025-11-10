🎮 Command-Line Tic-Tac-Toe 

This is a complete, two-player implementation of the classic $3 \times 3$ Tic-Tac-Toe game, built entirely in Python for the command line. This project focuses on robust input validation, clear state management, and an enhanced user interface experience.

✨ Key Features Implemented

Clean CLI Interface: Utilizes the os module to clear the console screen before every turn, preventing messy output and ensuring a smooth, single-board view.

Perfect Alignment: The $3 \times 3$ grid is formatted with precise spacing, ensuring the column headers (0 | 1 | 2) align perfectly with the playing cells for easy coordinate identification.

Robust Input Handling: Comprehensive error checking is implemented to prevent crashes from empty input, non-numeric characters, or out-of-bounds coordinate entries.

Modular Design: The game logic is divided into distinct functions for initialization, display, input, and win/tie checking, making the code easy to read and maintain.

🚀 How to Run the Game

Save the Code: Save the Python code provided in the source block below into a file named tic_tac_toe.py.

Open Terminal/Command Prompt: Navigate to the directory where you saved the file.

Execute: Run the script using the Python interpreter:

python tic_tac_toe.py


Play: Follow the prompts to choose your symbol ('X' or 'O') and enter your moves using Row and Column indices (0, 1, or 2).

💡 Code Breakdown and Logic

The game logic is structured into several key functions:

1. Board Initialization (create_board())

Initializes the game state. It uses a list comprehension to efficiently generate the $3 \times 3$ grid.

2. Display and UX (display_board() and clear_screen())

display_board(board): Handles all output formatting, using separator lines and calculated padding to ensure the row indices, column indices, and cell contents are perfectly aligned.

clear_screen(): Ensures a clean user experience by clearing the previous turn's output before rendering the new board state.

3. Input and Validation (player_input())

This function manages user input, looping until a valid, empty coordinate is chosen. It includes three layers of validation: Type Check, Bounds Check, and Occupancy Check.

4. Game Logic (check_win(), check_tie(), and play())

check_win(board, player): The core victory detection logic, checking all rows, columns, and both diagonals.

check_tie(board): Checks if the board is full.

play(): The main controller, managing the turn-based loop.

