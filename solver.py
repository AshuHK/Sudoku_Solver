def solve_board(board): 
  """
  Solves the board and checks if it is solved
  Parameters: board (2-D list of ints)
  Returns: boolean for if the board is solved 
  """
  first_empty_tuple = find_empty(board)
  if first_empty_tuple == (-1, -1): 
     return True
  else: 
    row_int, col_int = first_empty_tuple
  
  for i in range(1, 10): 
    if valid(board, i, (row_int, col_int)): 
      board[row_int][col_int] = i 

      if solve_board(board):
        return True 
      
      board[row_int][col_int] = 0 

  return False


def find_empty(board):
  """
  Finds first empty cell on the board
  Parameters: board (2-D list of ints)
  Return: tuple of two ints formmated (row, column)
  """
  for row in board: 
    for spot in row: 
      if spot == 0: 
        return (board.index(row), row.index(spot))
  
  return (-1, -1)

def valid(board, num_int, pos_tuple): 
  """
  Checks if the number is valide at a certain position 
  Parameters: board (2-D list of ints), num_int (int to insert), 
              pos_tuple [(row, col) pair of ints] 
  Return: boolean of if the number is valid at that position
  """
  # row check
  for i in range(len(board[0])): 
    if board[pos_tuple[0]][i] == num_int and pos_tuple[1] != i: 
      return False 

  # column check 
  for i in range(len(board)): 
    if board[i][pos_tuple[1]] == num_int and pos_tuple[0] != i: 
      return False 
  
  # cell check
  cell_x = pos_tuple[1] // 3  # column
  cell_y = pos_tuple[0] // 3  # row 

  for i in range(cell_y * 3, cell_y * 3 + 3): 
    for j in range(cell_x * 3, cell_x * 3 + 3): 
      if board[i][j] == num_int and (i,j) != pos_tuple: 
        return False

  return True
