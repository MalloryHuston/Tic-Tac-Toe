class TicTacToe:
    """
    A game of TicTacToe includes a board with nine spaces and its current win state.
    """

    def __init__(self):
        """
        Instantiates a new game of TicTacToe with nine blank spaces on the board and current_state "UNFINISHED".
        """
        self.board = [["","",""],["","",""],["","",""]]
        self.current_state = "UNFINISHED" # Possible states are "UNFINISHED", "X_WON", "O_WON", and "DRAW".

    def get_current_state(self):
        """
        Returns current_state
        """
        return self.current_state

    def make_move(self, row, column, player):
        """
        If the attempted move is valid:
        Marks the given row and column with the player's "x" or "o", updates current_state, then returns True.
        If the attempted move is not valid:
        Returns False.
        """
        if self.__check_valid_move(row, column):
            self.board[row][column] = player
            self.__update_current_state()
            return True
        else:
            return False

    def __check_valid_move(self, row, column):
        """
        Returns if the attempted move is valid.
        """
        # To make a valid move, the current_state cannot be a "DRAW", "X_WON", or "O_WON"
        if self.current_state == "UNFINISHED":
            # The board has three rows and three columns
            if 0 <= row <= 2 and 0 <= column <= 2:
                # The attempted space cannot already contain a move by "x" or "o"
                if self.board[row][column] == "":
                    return True
        return False

    def __update_current_state(self):
        """
        Checks board to determine if game_state should change by referencing all possible TicTacToe game solutions.
        """

        # A dictionary holds the keys "x" and "o" and those players' win state, assumed False until checked.
        # There is also the key "" for the case where a possible TicTacToe game solution is occupied entirely by "",
        # but the value associated with the key "" does not affect game_state.
        score = {
            "x" : False,
            "o" : False,
            ""  : False,
        }

        # Horizontal lines
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            score[self.board[0][0]] = True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]:
            score[self.board[1][0]] = True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]:
            score[self.board[2][0]] = True

        # Vertical lines
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]:
            score[self.board[0][0]] = True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]:
            score[self.board[0][1]] = True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]:
            score[self.board[0][2]] = True

        # Diagonal lines
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
            score[self.board[0][0]] = True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
            score[self.board[2][0]] = True

        # If "x" has three spaces in a row, change game_state to "X_WON"
        if score["x"]:
            self.current_state = "X_WON"
        # If "o" has three spaces in a row, change game_state to "O_WON"
        elif score["o"]:
            self.current_state = "O_WON"
        # If neither "x" nor "o" have three spaces in a row, if there are no remaining empty spaces on the board
        # change game_state to "DRAW"
        else:
            count_empty = 0
            for row in self.board:
                for column in row:
                    if column == "":
                        count_empty += 1
            if count_empty == 0:
                self.current_state = "DRAW"

    def __print_board(self):
        """
        For testing purposes, prints to the console a visual representation of board
        """
        print(self.board[0][0],"|",self.board[0][1],"|",self.board[0][2])
        print(self.board[1][0], "|", self.board[1][1], "|", self.board[1][2])
        print(self.board[2][0], "|", self.board[2][1], "|", self.board[2][2])

"""
Test code
game1 = TicTacToe()
game1.make_move(0,0,"x")
game1.make_move(0,1,"x")
game1.make_move(0,2,"x")
print(game1.current_state)
game2 = TicTacToe()
game2.make_move(0,0,"o")
game2.make_move(0,1,"x")
game2.make_move(0,2,"o")
game2.make_move(1,0,"x")
game2.make_move(1,1,"o")
game2.make_move(2,0,"x")
game2.make_move(1,2,"o")
game2.make_move(2,2,"x")
game2.make_move(2,1,"o")
print(game2.current_state)
game3 = TicTacToe()
game3.make_move(0,0,"o")
game3.make_move(1,1,"o")
game3.make_move(2,2,"o")
print(game3.current_state)
"""
