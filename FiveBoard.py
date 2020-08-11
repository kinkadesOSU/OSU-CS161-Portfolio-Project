# Author: Sam Kinkade
# Date: 8/30/20
# Description: Allows for the playing of a 15x15 board game where players must get 5 'x's or 'o's in a row, column, or diagonal.

class FiveBoard:
    """Creates the board game "rules" and checks for the winning conditions"""

    def __init__(self):
        """Creates an empty and defaults the game to unfinished"""
        # Fill board with empty strings (Rows = index 0-14, 15-29, etc. columns = index 0,15,10
        self._game_board = [["-" for x in range(0, 15)] for y in range(0, 15)]
        self._current_state = "UNFINISHED"  # can be X_WON, O_WON, DRAW, or UNFINISHED

    # def draw_board_with_draw(self):
    #     """Test method to fill the board with a draw game"""
    #     # Test to create a board with a draw
    #     for i in range(0, 15):
    #         for j in range(0, 15):
    #             if i == 14 and j ==14:
    #                 break
    #             else:
    #                 if i % 2 == 0 or i == 0:
    #                     if j % 3 == 0:
    #                         self._game_board[i][j] = 'o'
    #                     else:
    #                         self._game_board[i][j] = 'x'
    #                 elif i % 2 == 1:
    #                     if j % 3 == 0:
    #                         self._game_board[i][j] = 'x'
    #                     else:
    #                         self._game_board[i][j] = 'o'

    # def get_current_board(self):  # delete at final
    #     """Test method to print out the game board"""
    #     print("    0    1    2    3    4    5    6    7    8    9    10   11   12   13   14")
    #     for i in range(0, 15):
    #         if i < 10:
    #             print(str(i) + "  " + str(self._game_board[i]))
    #         else:
    #             print(str(i) + " " + str(self._game_board[i]))

    def get_current_state(self):
        """Returns the state of the game (won, draw, or unfinished"""
        return self._current_state

    def make_move(self, row, column, move):  # NEED A DRAW CONDITION
        """Allows for a player to make a move based on a row or column input"""
        # Checks if the position played in is blank or if the game is not finished

        if self._game_board[row][
            column] != "-" or self._current_state != "UNFINISHED":  # looks to see if the space is blank or if the game is unfinished
            # print(str(row) + ", " + str(column) + "played by " + move + " is invalid")
            return False
        else:
            # Update the board, check for a win condition, and update the state
            self._game_board[row][column] = move
            if ((self.check_horizontals(move) == 5) or
                    (self.check_verticals(move) == 5) or (self.check_diagonals(
                        move) == 5)):  # looks if there is any of the three win scenarios present
                # if the win condition is present, say who won
                if move == 'x':
                    self._current_state = 'X_WON'
                elif move == 'o':
                    self._current_state = 'O_WON'
            self.check_draw()
        return True

    def check_horizontals(self, check_move):
        """checks the rows for a winning set of 5"""
        move_count = 0
        for i in range(0, 14):  # loops through the rows
            for j in range(0, 14):  # loop through the columns
                if self._game_board[i][j] == check_move:
                    move_count += 1
                    if move_count == 5:
                        return move_count
                # if the move isn't present, we have to start the win count over again
                else:
                    move_count = 0
        return move_count

    def check_verticals(self, check_move):
        """checks the columns for a winning set of 5"""
        move_count = 0
        for j in range(0, 14):  # loop through the columns
            for i in range(0, 14):  # loop through the rows
                if self._game_board[i][j] == check_move:
                    move_count += 1
                    if move_count == 5:
                        return move_count
                # if the move isn't present, we have to start the win count over again
                else:
                    move_count = 0
        return move_count

    def check_diagonals(self, check_move):
        """checks the diagonals for a winning set of 5"""
        # check diagonals to the left
        move_count = 0
        for i in range(0, 14):
            for j in range(0, 14):
                try:
                    if self._game_board[i][j] == check_move:
                        move_count += 1
                        i += 1  # skip down an extra row to stay on the diagonal
                        if move_count == 5:
                            return move_count
                    # if the move isn't present, we have to start the win count over again
                    else:
                        move_count = 0
                except IndexError:
                    continue
        move_count = 0
        for i in range(0, 14, 1):
            for j in range(14, 0, -1):
                try:
                    if self._game_board[i][j] == check_move:
                        move_count += 1
                        i += 1  # skip down an extra row to stay on the diagonal
                        if move_count == 5:
                            return move_count
                    # if the move isn't present, we have to start the win count over again
                    else:
                        move_count = 0
                except IndexError:
                    continue
        return move_count

    def check_draw(self):
        """Checks if there is a draw (no empty spaces left)"""
        is_draw = True  # assume it is a draw
        for i in range(0, 15):
            for j in range(0, 15):
                if self._game_board[i][j] == "-":  # if a blank space is found, the game can't be a draw
                    is_draw = False
                    return is_draw
        if is_draw:
            self._current_state = "DRAW"  # changes the state
        return is_draw


# board = FiveBoard()
# board.draw_board_with_draw()
# print(board.get_current_board())
# print(board.is_draw())
# board.make_move(14, 14, 'x')
# print(board.get_current_state())

# while board.get_current_state() == "UNFINISHED":
#     # computer player
#     row = random.randint(0, 14)
#     col = random.randint(0, 14)
#     move = 'x'
#     print("x played " + str(row) + ", " + str(col))
#     board.make_move(row, col, move)
#     # print(board.get_current_state())
#
#     row = random.randint(0, 14)
#     col = random.randint(0, 14)
#     move = 'o'
#     print("o played " + str(row) + ", " + str(col))
#     board.make_move(row, col, move)
#
# print(board.get_current_board())
# print(board.get_current_state())
