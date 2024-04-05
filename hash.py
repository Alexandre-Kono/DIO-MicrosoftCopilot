def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    if [player, player, player] in win_conditions:
        return True
    return False

def get_move(player):
    while True:
        move = input(f"Player {player}, enter your move (row col): ")
        row, col = move.split()
        row, col = int(row) - 1, int(col) - 1
        if 0 <= row <= 2 and 0 <= col <= 2:
            return row, col
        else:
            print("Invalid move. Try again.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves_count = 0

    while moves_count < 9:
        print_board(board)
        row, col = get_move(current_player)
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
            moves_count += 1
        else:
            print("That space is already taken. Try again.")

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    main()
