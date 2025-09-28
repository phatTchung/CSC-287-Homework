def print_board(board):
    """
    Show the tic-tac-toe board on the screen.
    """
    for row in board:
        print(" | ".join(row))
    print()


def check_winner(board, player):
    """
    Check if the given player (X or O) has won.
    Returns True if they win, False if not.
    """
    # check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def play_game():
    """
    Run one game of tic-tac-toe for two players.
    Handles moves, checks winner, and checks draw.
    """
    # 2D board (dimensional array)
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Your move, {current_player} (1–9): ")

        if not (move.isdigit() and 1 <= int(move) <= 9):
            print("Invalid move! Pick 1–9.")
            continue

        num = int(move) - 1
        row, col = divmod(num, 3)

        if board[row][col] in ["X", "O"]:
            print("Spot already taken!")
            continue

        board[row][col] = current_player

        # winner?
        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} is the winner!")
            break

        # draw?
        if all(board[r][c] in ["X", "O"] for r in range(3) for c in range(3)):
            print_board(board)
            print("It's a draw!")
            break

        # switch turn
        current_player = "O" if current_player == "X" else "X"


while True:
    play_game()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
