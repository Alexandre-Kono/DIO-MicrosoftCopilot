# DIO-MicrosoftCopilot
Generative AI with Microsoft Copilot

https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/12-generative-ai.html

– https://copilot.microsoft.com/

# Imagens geradas por IA

![image](https://github.com/Alexandre-Kono/DIO-MicrosoftCopilot/assets/142547742/bc0d0bc9-8da7-4731-bbd1-cfbe2bedce59)

![image](https://github.com/Alexandre-Kono/DIO-MicrosoftCopilot/assets/142547742/f2353d14-cd33-4214-abed-b850da0aadc4)

![image](https://github.com/Alexandre-Kono/DIO-MicrosoftCopilot/assets/142547742/5168df2e-b2cc-4d4e-8288-756f65dde0ec)


# Código para jogo da velha

Após solicitar código em Python.

````python
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
````
![image](https://github.com/Alexandre-Kono/DIO-MicrosoftCopilot/assets/142547742/0537a998-dc26-44d3-8e41-4aced5e923e9)

Após solicitar para alterar o código para html.

````html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tic-Tac-Toe Game</title>
<style>
  .board { display: grid; grid-template-columns: repeat(3, 100px); grid-gap: 10px; }
  .cell { width: 100px; height: 100px; background-color: #f0f0f0; display: flex; justify-content: center; align-items: center; cursor: pointer; font-size: 2em; }
  .hidden { display: none; }
</style>
</head>
<body>
<div id="gameBoard" class="board">
  <!-- The 9 cells of the tic-tac-toe board -->
  <div class="cell" onclick="makeMove(this, 0)"></div>
  <div class="cell" onclick="makeMove(this, 1)"></div>
  <div class="cell" onclick="makeMove(this, 2)"></div>
  <div class="cell" onclick="makeMove(this, 3)"></div>
  <div class="cell" onclick="makeMove(this, 4)"></div>
  <div class="cell" onclick="makeMove(this, 5)"></div>
  <div class="cell" onclick="makeMove(this, 6)"></div>
  <div class="cell" onclick="makeMove(this, 7)"></div>
  <div class="cell" onclick="makeMove(this, 8)"></div>
</div>
<p id="winner" class="hidden"></p>

<script>
let currentPlayer = 'X';
let board = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;

function makeMove(cell, index) {
  if (board[index] !== '' || !gameActive) {
    return;
  }
  board[index] = currentPlayer;
  cell.textContent = currentPlayer;
  checkWinner();
  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}

function checkWinner() {
  const winConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]             // Diagonals
  ];

  for (let i = 0; i < winConditions.length; i++) {
    const [a, b, c] = winConditions[i];
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      document.getElementById('winner').textContent = `Player ${currentPlayer} wins!`;
      document.getElementById('winner').classList.remove('hidden');
      gameActive = false;
      return;
    }
  }

  if (!board.includes('')) {
    document.getElementById('winner').textContent = 'It\'s a tie!';
    document.getElementById('winner').classList.remove('hidden');
    gameActive = false;
  }
}
</script>
</body>
</html>
````
![image](https://github.com/Alexandre-Kono/DIO-MicrosoftCopilot/assets/142547742/f3adf85a-7d85-488e-8d00-a32a863acfac)

# Tarefa bônus
What are 3 examples of generative AI helping people?

![image](https://github.com/Alexandre-Kono/DIO-MicrosoftCopilot/assets/142547742/9f1d16cb-2a5d-4fcb-9aa1-afe9c9ae1b3d)


