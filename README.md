# Tic-Tac-Toe
This program initializes a class that creates the <a href="https://en.wikipedia.org/wiki/Tic-tac-toe">Tic-tac-toe</a> board and checks for winning scenarios after each move. The game prompts the user for a row and column space in which to write down an "x" or "o" of the current player. The "x" or "o" is then left in an open space where appropriate. Whichever player gets all three of their "x's" or "o's" all in the same horizontal, vertical, or diagonal line first wins the game.

Write a class named TicTacToe that has two private data members: the board, which will be a list of lists that represent a 3x3 board, and the current state. It should have a get method named get_current_state.

The class should have an init method that initializes the board to a list of three lists that each contain three empty strings (where each represents an empty square), and initializes the current_state to "UNFINISHED".

It should have a method named make_move that takes three parameters, a row and a column (in that order) where each is an integer in the range 0-2, and either 'x' or 'o' to indicate the player who is making the move. If the row or column are out of bounds, or if that square is already occupied, or if the game has already been won or drawn, make_move should return False. Otherwise, it should record the move, update current_state to the appropriate value, and return True. The possible values of current_state are: "X_WON", "O_WON", "DRAW", or "UNFINISHED". It's possible for multiple moves to be made in a row for the same player. A game is drawn when all of the squares are filled, but neither player has won.

It's not required, but you'll probably find it useful for testing and debugging to have a method that prints out the board.

Whether you think of the array indices as being [row][column] or [column][row] doesn't matter as long as you're consistent.

Your file must be named: ```TicTacToe.py```
