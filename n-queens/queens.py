class BoardPosition:
  def __init__(self, row, column):
    self.row = row
    self.column = column

  def __eq__(self, other):
    return self.row == other.row and     \
           self.column == other.column

  def __ne__(self, other):
    return not self.__eq__(other)

class ChessBoard:
  def __init__(self, queens_placement):
    self.queen_positions = []
    for row, column in enumerate(queens_placement):
      self.queen_positions.append(BoardPosition(row, column))

  def get_number_of_collisions(self):
    collisions = 0
    
    for queen_a in self.queen_positions:
      for queen_b in self.queen_positions:
        if queen_a == queen_b:
          continue

        if ChessBoard.queens_collide(queen_a, queen_b):
          collisions += 1

    # Since collisions are counted twice for each pair,
    # dividing by two normalizes this result.
    collisions = collisions // 2

    return collisions

  @staticmethod
  def queens_collide(queen_a, queen_b):
    """
      Return whether the two given queens
      can attack each other, based on their
      positions on the board.
    """
    return queen_a.row == queen_b.row or                                           \
           queen_a.column == queen_b.column or                                     \
           abs(queen_a.row - queen_b.row) == abs(queen_a.column - queen_b.column)

  @staticmethod
  def coordinate_to_chess_notation(row, column, number_of_queens):
    column_identifier = chr(ord('a') + column)
    row_identifier = str(number_of_queens - row)
    return column_identifier + row_identifier 