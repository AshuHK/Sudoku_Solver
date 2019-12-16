# for testing purposes 

def find_empty(board):
  """
  Finds first empty cell on the board
  Parameters: board (2-D list of ints)
  Return: tuple of two ints formmated (row, column)
  """
  for row in board: 
    for cell in row: 
      if cell == 0: 
        return (board.index(row), row.index(cell))
  
  return (-1, -1)


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
  # print(find_empty(board))

  pass


if __name__ == "__main__": 
  main()
