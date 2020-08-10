# Author: Sam Kinkade
# Date: 
# Description:

class FiveBoard:

    def __init__(self):
        # Fill board with empty strings (Rows = index 0-14, 15-29, etc. columns = index 0,15,10
        self._game_board = [["-" for x in range(0, 15)] for y in range(0, 15)]
        self._current_state = "UNFINISHED"  # can be X_WON, O_WON, DRAW, or UNFINISHED

    def get_current_board(self):  # delete at final
        print("    0    1    2    3    4    5    6    7    8    9    10   11   12   13   14")
        for i in range(0, 15):
            print(str(i) + " " + str(self._game_board[i]))

    def get_current_state(self):
        return self._current_state

    def make_move(self, row, column, move):  # NEED A DRAW CONDITION
        # Checks if the position played in is blank or if the game is not finished
        if self._game_board[row][column] != "-" or self._current_state != "UNFINISHED":
            return False
        else:
            # Update the board, check for a win condition, and update the state
            self._game_board[row][column] = move
            if (self.check_horizontals(move) == 5) or (
                    self.check_verticals(move) == 5) or (self.check_diagonals(move) == 5):
                if move == 'x':
                    self._current_state = 'X_WON'
                elif move == 'o':
                    self._current_state = 'O_WON'
                return True

    def check_horizontals(self, move):
        move_count = 0
        for i in range(0, 14):
            for j in range(0, 14):
                if self._game_board[i][j] == move:
                    move_count += 1
                    if move_count == 5:
                        return move_count
                else:
                    move_count = 0
        return move_count

    def check_verticals(self, move):
        move_count = 0
        for j in range(0, 14):
            for i in range(0, 14):
                if self._game_board[i][j] == move:
                    move_count += 1
                    if move_count == 5:
                        return move_count
                else:
                    move_count = 0
        return move_count

    def check_diagonals(self, move):
        # check diagonals to the left
        move_count = 0
        for i in range(0, 14):
            for j in range(0, 14):
                if self._game_board[i][j] == move:
                    move_count += 1
                    i += 1
                    if move_count == 5:
                        return move_count
                else:
                    move_count = 0
        move_count = 0
        for i in range(0, 14, 1):
            for j in range(14, 0, -1):
                if self._game_board[i][j] == move:
                    move_count += 1
                    i += 1
                    if move_count == 5:
                        return move_count
                else:
                    move_count = 0
        return move_count

# board = FiveBoard()
# board.make_move(0, 0, 'x')
# board.make_move(0, 0, 'o')
# board.make_move(2, 12, 'x')
# board.make_move(3, 11, 'x')
# board.make_move(4, 10, 'x')
# print(board.get_current_board())
# print(board.get_current_state())
#
# while board.get_current_state() == "UNFINISHED":
#     row = int(input("Input a row to play: "))
#     col = int(input("Input a column to play: "))
#     move = input("Enter a move (x or o) to play: ")
#     board.make_move(row, col, move)
#     print(board.get_current_board())
#     print(board.get_current_state())
