# for testing purposes 

def solve_board(board): 

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

def print_board(board):
  """
  Prints the board
  Parameters: board (2-D list of ints)
  Return: None
  """ 

  for i in range(len(board)): 
    if i % 3 == 0 and i != 0: 
      print("-----------------------")

    for j in range(len(board[0])): 
      if j % 3 == 0 and j != 0: 
        print(" | ", end = "")
      
      if j == 8: 
        print(board[i][j], end = "\n")
      else: 
        print(str(board[i][j]) + " ", end = "")
  pass

def main(): 
  board=[[3,0,6,5,0,8,4,0,0], 
         [5,2,0,0,0,0,0,0,0], 
         [0,8,7,0,0,0,0,3,1], 
         [0,0,3,0,1,0,0,8,0], 
         [9,0,0,8,6,3,0,0,5], 
         [0,5,0,0,9,0,6,0,0], 
         [1,3,0,0,0,0,2,5,0], 
         [0,0,0,0,0,0,0,7,4], 
         [0,0,5,2,0,6,3,0,0]] 
  print(" ----Original Board----") 
  print_board(board) 

  solve_board(board) 
  print("\n ----Solved Board----")
  print_board(board)
  # print(find_empty(board))

  pass


if __name__ == "__main__": 
  main()
