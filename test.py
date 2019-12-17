# this file is for testing purposes 

# this is to check if the solving takes too long
import time 

def generate_board(): 
  """
  Randomly generate a board 
  Parameters: None 
  Return: board (2-D list of ints)
  """
  board = [[0 for x in range(9)]for y in range(9)] 
  return board

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
  board = generate_board()
  print(" ----Original Board----") 
  print_board(board) 
  # solve_board(board) 

  # print("\n ----Solved Board----")
  # print_board(board)
  # print(find_empty(board))

  pass


if __name__ == "__main__": 
  main()
