# import solver
from kivy.app import App
from kivy.core.window import Window 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class SudokuWindow(App):
    def build(self):
        app_layout = GridLayout(cols = 9, rows = 9)
        board=[[3,0,6,5,0,8,4,0,0], 
               [5,2,0,0,0,0,0,0,0], 
               [0,8,7,0,0,0,0,3,1], 
               [0,0,3,0,1,0,0,8,0], 
               [9,0,0,8,6,3,0,0,5], 
               [0,5,0,0,9,0,6,0,0], 
               [1,3,0,0,0,0,2,5,0], 
               [0,0,0,0,0,0,0,7,4], 
               [0,0,5,2,0,6,3,0,0]] 
        
        for row in board: 
            for num in row: 
                if num != 0: 
                    app_layout.add_widget(Button(text = str(num)))
                else: 
                    app_layout.add_widget(Button(text = ""))
        return app_layout


    # def solve_board(self, app_layout, board): 
    #     return False
        
    
    # def find_empty(self, board): 
    #     return (-1, -1)
    

    # def valid(self, board, num_int, pos_tuple): 
    #     return True


if __name__ == "__main__": 
    SudokuWindow().run()
